from fastapi import FastAPI, HTTPException
from Process import ProcessItem
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

processArr = [
    {
        'name':'A',
        'cpu_time':3,
        'arrival':0
    },
    {
        'name':'B',
        'cpu_time':4,
        'arrival':0
    },
    {
        'name':'C',
        'cpu_time':2,
        'arrival':0
    },
    {
        'name':'D',
        'cpu_time':6,
        'arrival':0,
        'priority':1
    }
]


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
    response = []
    for process in processArr:
        response.append(ProcessItem(**process))

    return response

@app.post('/api/process')
def create_process_array(pList: List[ProcessItem]):
    try:
        print(pList)
        response = pList
        return f'success, data:{response}'
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))