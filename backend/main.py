from fastapi import FastAPI, HTTPException
from Process import ProcessItem
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError


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
        print(f'request: {pList}')
        response = pList
        return f'success, data:{response}'
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))