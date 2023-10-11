from Process import ProcessItem
from typing import List
from Process import ProcessItem
import pandas as pd

class ProcessManagement:
    def __init__(self, data: List[ProcessItem], method: str) -> None:
        self.data = data
        self.method = method
        self.wait = []
        self.time_df = None

    
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
        
        return self.to_DataFrame(solution)
        


    def RoudRobin(self, quantum: int = 1, ctxt: int = 1):
     
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

    def toDataFrame(self, l):
        d = {}
        for i in range(len(l)):
            d[str(i)]=pd.Series(l[i])

        df = pd.DataFrame(d)

        self.time_df= self.CreateDataTimes(df)

        df = df.transpose()
        json_df = df.to_json()
        
        return json_df
    
    def mean(self, dic):
        cont = 0
        for num in dic:
            cont+=dic[num]

        return cont/len(dic)

    def TimeReturn(self, df):
        time_return={}

        for col in df:
            for fila in df[col]:
                if not pd.isna(fila):
                    for process in range(len(self.data)):
                        if fila[0]==self.data[process]["name"]:
                            if not str(fila[0]) in time_return:
                                time_return[fila[0]]=1
                            else:
                                time_return[fila[0]]+=1
        time_tuplas=[]               
        for process in time_return:
            time_tuplas.append((process,time_return[process]))

        return time_tuplas 

    def TimeWait(self, df):
        time_wait = {}
        aux = df[1:]
        for col in aux:
            for fila in aux[col]:
                if not pd.isna(fila):
                    for process in range(len(self.data)):
                        if fila[0]==self.data[process]["name"]:
                            if not str(fila[0]) in time_wait:
                                time_wait[fila[0]] = 1
                            else:
                                time_wait[fila[0]] += 1
                            
        time_tuplas=[]               
        for process in time_wait:
            time_tuplas.append((process,time_wait[process]))
        time_tuplas.append(("PROMEDIO",self.mean(time_wait)))

        return time_tuplas 
    
    def CreateDataTimes(self, df):
        tr=self.TimeReturn(df)
        tw=self.TimeWait(df)

        l = [tr,tw]
        d={}
        for i in range(len(l)):
            d[str(i)]=pd.Series(l[i])

        df = pd.DataFrame(d)
        df = df.transpose()
        json_df = df.to_json()
        
        return json_df

    


    

