from Process import ProcessItem
from typing import List

class ProcessManagement:
    def __init__(self, data: List(ProcessItem), method: str) -> None:
        self.data = data
        self.method = method
    
    def generateGantt(self):
        pass

    def RoudRobin(self, quantum: int = 1, ctxt: int = 1, prio=False):
        pass
    
    def FCFS(self, ctxt: int = 0):  # First Come First Serve
        pass

    def Priority(self, ctxt: int = 0):
        pass

    def SJF(self, ctxt: int = 0):  # Shortest Job First
        pass

    def SRT(self, ctxt: int = 0):  # Shortest Remaining Time
        pass

