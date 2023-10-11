
from pydantic import BaseModel
from typing import List
from Process import ProcessItem

# Define a Pydantic model matching the expected structure
class ProcessData(BaseModel):
    data: List[ProcessItem]
    method: str
