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
        ProcessItem(**{'name':'A','cpu_time':4,'arrival':0}),
        ProcessItem(**{'name':'B','cpu_time':3,'arrival':1}),
        ProcessItem(**{'name':'C','cpu_time':2,'arrival':2}),
    ]

    # data = []
    # for item in incoming:
    #     data.append(ProcessItem(**item))

    
    sol = ProcessManagement(data, 'FCFS')
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