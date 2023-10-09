from pydantic import BaseModel

class ProcessItem(BaseModel):
    name: str
    cpu_time: int
    arrival: int
    priority: int
    
# class Process(BaseModel):
#     name: str = ''
#     cpu_time: int = 0
#     arrival: int = 0
#     remaining_time: int = 0
#     priority: int = -1

#     def __init__(self, **data):
#         super().__init__(**data)
#         self.remaining_time = self.cpu_time

