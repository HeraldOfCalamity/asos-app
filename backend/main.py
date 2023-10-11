from fastapi import FastAPI, HTTPException
from Process import ProcessItem
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from ProcessManagement import ProcessManagement

app = FastAPI()

origins = [ 'http://localhost:5173' ]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.get('/')
def read_root():
    return {'message': 'Everything ok!'}


@app.get('/api/process')
def get_all_process():
    data = [
        ProcessItem(**{'name':'A','cpu_time':10,'arrival':8, 'priority':9}),
        ProcessItem(**{'name':'B','cpu_time':1,'arrival':5, 'priority':2}),
        ProcessItem(**{'name':'C','cpu_time':6,'arrival':4, 'priority':5}),
        ProcessItem(**{'name':'D','cpu_time':7,'arrival':12, 'priority':3}),
        ProcessItem(**{'name':'E','cpu_time':12,'arrival':25, 'priority':1}),
    ]

    # data = []
    # for item in incoming:
    #     data.append(ProcessItem(**item))

    
    sol = ProcessManagement(data, 'SRT')
    a = sol.generateGantt()
    print(f'------------------------------------------------ Response ------------------------------------------------\n{a}')
    # print(a)
    
    # print(sol.data)
    return a

@app.post('/api/process')
def create_process_array(pList: List[ProcessItem]):
    try:
        print(f'request: {pList}')
        response = pList
        return f'success, data:{response}'
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))