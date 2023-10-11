from Process import ProcessItem
from typing import List
from Process import ProcessItem
import copy
import pandas as pd

class ProcessManagement:
    def __init__(self, data: List[ProcessItem], method: str) -> None:
        self.data = data
        self.method = method
        self.wait = []
        self.time_df = None
        self.currentProcess = ('0', 0)

    
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
        
        return self.toDataFrame(solution)
        


    def RoudRobin(self, quantum: int = 1, ctxt: int = 1):
        pass
    
    def proToWait(self, index: int):
        for process in self.data:
            # print(f'process: {process.name}, arrival: {process.arrival}, index: {index}')
            if process.arrival == index:
                # print(f'process: {process.name} appened to queue at time: {index}')
                self.wait.append((process.name, process.remaining_time))
        
                
    


    def FCFS(self, ctxt: int = 0) -> list:   # First Come First Serve
        df = []
        time = 0
        end = False

        while True:
            print(f'<=========================>\n - Time: {time} -')
            col = []

            if self.wait and (self.currentProcess[1] == 1 or self.currentProcess[1] == 0):
                self.currentProcess = self.wait.pop(0)
            elif self.currentProcess[1] > 1:
                self.currentProcess = (self.currentProcess[0], self.currentProcess[1] - 1)


            self.proToWait(time)

            print(f'currentProcess: {self.currentProcess}')
  
            currentWait = copy.deepcopy(self.wait)
            
            # Excecution Zone
            if currentWait:
                print(f'currentWait: {currentWait}')
            else:
                end = True
    

            col.append(self.currentProcess)
            # Wait queue Zone
            col.append(currentWait)

            # Column appending Zone
            df.append(col)
            print('<=========================>')
            time += 1


            if self.currentProcess[1] == 1 and end:
                break
            
        return df

    

    def byPriority(self, ord: str="SMALLEST"):
        # Create a key function to sort by priority
        key_function = lambda process: process.priority

        if ord == "GREATEST":
            reverse = True
        elif ord == "SMALLEST":
            reverse = False
        else:
            raise ValueError("Invalid value for 'ord'. Use 'SMALLEST' or 'GREATEST'.")

        # Sort the data based on priority
        sorted_data = sorted(self.data, key=key_function, reverse=reverse)

        # Create a list of tuples (name, remaining_time)
        self.wait = [(process.name, process.remaining_time) for process in sorted_data]

        


        


    def Priority(self, ctxt: int = 0, ord:str = 'SMALLEST'):
        df = []
        time = 0
        end = False

        while True:
            print(f'<=========================>\n - Time: {time} -')
            col = []

            if self.wait and (self.currentProcess[1] == 1 or self.currentProcess[1] == 0):
                self.currentProcess = self.wait.pop(0)
            elif self.currentProcess[1] > 1:
                self.currentProcess = (self.currentProcess[0], self.currentProcess[1] - 1)

            if time == 0:
                self.byPriority(ord)

            print(f'currentProcess: {self.currentProcess}')
  
            currentWait = copy.deepcopy(self.wait)
            
            # Excecution Zone
            if currentWait:
                print(f'currentWait: {currentWait}')
            else:
                end = True
    

            col.append(self.currentProcess)
            # Wait queue Zone
            col.append(currentWait)

            # Column appending Zone
            df.append(col)
            print('<=========================>')
            time += 1


            if self.currentProcess[1] == 1 and end or time == 10:
                break
            
        return df



    def byCPUTime(self):
        # Create a key function to sort by CPU time
        key_function = lambda process: process.cpu_time

        # Sort the data based on CPU time in ascending order
        sorted_data = sorted(self.data, key=key_function)

        # Create a list of tuples (name, remaining_time)
        self.wait = [(process.name, process.remaining_time) for process in sorted_data]



    def SJF(self, ctxt: int = 0):  # Shortest Job First
        df = []
        time = 0
        end = False
        while True:
            print(f'<=========================>\n - Time: {time} -')
            col = []

            if self.wait and (self.currentProcess[1] == 1 or self.currentProcess[1] == 0):
                self.currentProcess = self.wait.pop(0)
            elif self.currentProcess[1] > 1:
                self.currentProcess = (self.currentProcess[0], self.currentProcess[1] - 1)

            if time == 0:
                self.byCPUTime()

            print(f'currentProcess: {self.currentProcess}')
  
            currentWait = copy.deepcopy(self.wait)
            
            # Excecution Zone
            if currentWait:
                print(f'currentWait: {currentWait}')
            else:
                end = True
    

            col.append(self.currentProcess)
            # Wait queue Zone
            col.append(currentWait)

            # Column appending Zone
            df.append(col)
            print('<=========================>')
            time += 1


            if self.currentProcess[1] == 1 and end:
                break
            
        return df

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
                    for process in self.data:
                        if str(fila[0])==process.name:
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

    


    

