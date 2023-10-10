from Process import ProcessItem
from typing import List
from Process import ProcessItem

class ProcessManagement:
    def __init__(self, data: List[ProcessItem], method: str) -> None:
        self.data = data
        self.method = method
        self.wait = []
    
    def generateGantt(self, method: str = None) -> list:
        solution = None

        # To change method
        if method:
            self.method = method

        if self.method == 'FCFS':
            solution = self.FCFS()
        elif self.method == 'RR':
            solution = self.RoudRobin()
        elif self.method == 'PRIO':
            solution = self.Priority()
        elif self.method == 'SJF':
            solution = self.SJF()
        elif self.method == 'SRT':
            solution = self.SRT()
        
        return solution
        


    def RoudRobin(self, quantum: int = 1, ctxt: int = 1):
        df = [
            ('A', 'remaining_time'), """en ejecucion"""
            ('xd xdxd'),  """ en espera """
            ('xd xdxd'),
            ('xd xdxd')
        ]
        pass
    
    def FCFS(self, ctxt: int = 0) -> list:   # First Come First Serve
        df = []
        time = 0

        for process in self.data:
                if process.arrival == time:
                    self.wait.append(process)

        # while True:
            
            

        #     break
            

        # while process.remaining_time > 0:
        #     if int(process.arrival) == time:
        #     # print(df)
        #         ex = (process.name, process.remaining_time)
        #         process.remaining_time -= 1    
        #     else:
        #         ex = ('0', 0)

        #     df.append(ex)
        #     time += 1

        return self.wait

    def Priority(self, ctxt: int = 0):
        pass

    def SJF(self, ctxt: int = 0):  # Shortest Job First
        pass

    def SRT(self, ctxt: int = 0):  # Shortest Remaining Time
        pass

