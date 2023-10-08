from fastapi import FastAPI
from Process import Process
from typing import List

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


@app.get('/')
def read_root():
    return {'message': 'Everything ok!'}


@app.get('/api/process')
def get_all_process():
    response = []
    for process in processArr:
        response.append(Process(**process))

    return response

@app.post('/api/process', response_model=str)
def create_process_array(pList: List[Process]):
    response = pList
        
    return f'success {response}'