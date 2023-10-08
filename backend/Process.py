from pydantic import BaseModel

class Process(BaseModel):
    name: str = ''
    cpu_time: int = 0
    arrival: int = 0
    remaining_time: int = cpu_time
    priority: int = -1
