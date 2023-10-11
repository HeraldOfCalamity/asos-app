from fastapi import FastAPI, HTTPException
from Process import ProcessItem
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from ProcessManagement import ProcessManagement
from Data import ProcessData

app = FastAPI()

origins = [ 'http://localhost:5173' ]

Gantt = ProcessManagement(None, None)


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
    # data = [
    #     ProcessItem(**{'name':'A','cpu_time':10,'arrival':8, 'priority':9}),
    #     ProcessItem(**{'name':'B','cpu_time':1,'arrival':5, 'priority':2}),
    #     ProcessItem(**{'name':'C','cpu_time':6,'arrival':4, 'priority':5}),
    #     ProcessItem(**{'name':'D','cpu_time':7,'arrival':12, 'priority':3}),
    #     ProcessItem(**{'name':'E','cpu_time':12,'arrival':25, 'priority':1}),
    # ]

    # data = []
    # for item in incoming:
    #     data.append(ProcessItem(**item))
    
    
    print(f'GET: Gantt data: {Gantt.data}')
    try:
        if Gantt is not None:
            response = Gantt.generateGantt()
        else:
            response = 'Gantt not created'
        # print(f'request: {pList}'
        
        print(f'------------------------------------------------ Response ------------------------------------------------\n{response}')
        
        return f'success, data:{response}'
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
# {
#     "data": [
#         {
#             "name": "A",
#             "cpu_time": "4",
#             "arrival": "0",
#             "priority": "7"
#         },
#         {
#             "name": "B",
#             "cpu_time": "4",
#             "arrival": "1",
#             "priority": "7"
#         },
#         {
#             "name": "C",
#             "cpu_time": "5",
#             "arrival": "2",
#             "priority": "8"
#         },
#         {
#             "name": "D",
#             "cpu_time": "8",
#             "arrival": "3",
#             "priority": "89"
#         }
#     ],
#     "method": "FCFS"
# }
@app.post('/api/process')
def create_process_array(pList: ProcessData):
    print(f'Incoming data: {pList}')

    try:
        print(f'request: {pList}')

        Gantt.data = pList.data
        Gantt.method = pList.method
        print(f'Gantt data: {Gantt.data}')
        return f'success, data:{pList}'
    except ValidationError as e:
        print(f'error: {pList}')
        raise HTTPException(status_code=422, detail=str(e))