from Process import ProcessItem
from typing import List
from Process import ProcessItem
import copy
import pandas as pd
class ProcessManagement:
    def __init__(self, data: List[ProcessItem], method: str) -> None:
        self.data = data
        self.method = method
        self.wait = None
        self.currentProcess = None  # al finalizar proceso reiniciar
        self.quantum = 3
        self.time_df = None
        self.ctxt = 0

    
    def generateGantt(self, method: str = None, ctxt: int = 0, quantum: int = 3) -> list:
        solution = None

        # To change method
        if method:
            self.method = method

        if ctxt != 0 and ctxt > 0:
            self.ctxt = ctxt
        if quantum != 3 and quantum > 0:
            self.quantum = quantum

        if self.method == 'FCFS':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.arrival})
        elif self.method == 'RR':
            solution = self.RoudRobin({'name':self.method, 'ord':lambda process: process.arrival, 'quantum':self.quantum, 'ctxt':self.ctxt})
        elif self.method == 'PRIO_sm' or self.method == 'PRIO_gt':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.priority})
        elif self.method == 'SJF':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.cpu_time})
        elif self.method == 'SRT':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.arrival})
        else:
            solution = [f'-- Error: method {self.method} does not exist --']
        
        return self.toDataFrame(solution)
        
                
    def checkFinish(self, pro: ProcessItem):
        if pro.remaining_time == 1:
            pro.done = True


    def isProcessingDone(self):
        for process in self.data:
            if not process.done:
                return False
        
        return True

    def rotateWait(self):
        if not self.wait:
            print(f'self.wait value: {self.wait}')
            return self.wait  # Return an empty list if the input list is empty
        print(f'Rotacion efectuada')
        return self.wait[1:] + [self.wait[0]]

    def restart(self):
        self.currentProcess = None
        self.wait = None
        for process in self.data:
            process.remaining_time = process.cpu_time
            process.done = False

    def baseAlgorithm(self, method) -> list:   # First Come First Serve
        df = []
        waitQueue = []
        time = 0

        if method['name'] == 'PRIO_gt':
            self.wait = sorted(self.data, key=method['ord'], reverse=True)
            print('\n\n====== prio invertida, de mayor a menor ==========\n\n')
        else:
            self.wait = sorted(self.data, key=method['ord'])
            print('ORODENACION NORMAL')

        print(f'\nEspera inicial: { self.wait}\n')
        
        while True:
            print(f'\n<------ time = {time} ------->')
            print(f'Current: {self.currentProcess}')
            column = []
            
            #setting the col wait queue
            if method['name'] == 'FCFS' or method['name'] == 'SRT':
                for waiting in self.wait:
                    if waiting.arrival == time:
                        waitQueue.append(waiting)
                        self.wait = self.rotateWait()

            elif method['name'][0:4] == 'PRIO' or method['name'] == 'SJF':
                waitQueue = self.wait

            # Appending of process in excecution
            if self.currentProcess is None:
                column.append(('0', 0))
            else:
                column.append((self.currentProcess.name, self.currentProcess.remaining_time))

            # Appending of current waiting queue
            column.append([(p.name, p.remaining_time) for p in copy.deepcopy(waitQueue)])

            # Appending of column i in df
            df.append(column)

            # End of time i
            print(f'<------------------------------>')
            time += 1

            # Executing process if exists and checking if its done
            if self.currentProcess is not None and not self.currentProcess.done:
                self.checkFinish(self.currentProcess)
                if method['name'] == 'SRT':
                    if waitQueue:
                        
                        waitQueue = sorted(waitQueue, key=lambda process: process.remaining_time)
                        print(f'SRT: currentProcess ({self.currentProcess.name}, {self.currentProcess.remaining_time}) next: ({waitQueue[0].name}, {waitQueue[0].remaining_time})')
                        if self.currentProcess.remaining_time > waitQueue[0].remaining_time:
                            self.currentProcess.remaining_time -= 1
                            waitQueue.append(self.currentProcess)
                            self.currentProcess = None
                            print(f'waitqueue: {waitQueue}')

                if self.currentProcess is not None:
                    self.currentProcess.remaining_time -= 1
                    print(f'Process {self.currentProcess.name} executed: {self.currentProcess.remaining_time}')

                    if self.currentProcess.done:
                        print(f'Process {self.currentProcess.name} done: {self.currentProcess.done}')
                        self.currentProcess = None

            # If process awaiting and no current process, from waiting queue to execution queue
            if waitQueue and self.currentProcess is None:
                self.currentProcess = waitQueue.pop(0)
                print(f'Current changed to: {self.currentProcess.name} remaining: {self.currentProcess.remaining_time}')

            # Checking if all process are done
            if self.isProcessingDone():
                print('------------------------------------------------------------')
                print(f'\nProcessing with {method["name"]} done')
                print(f'data before restart:\n {self.data}')
                self.restart()
                print(f'data after restart:\n {self.data}')
                print('------------------------------------------------------------')
                break

        return df

    def RoudRobin(self, method: dict):
        df = []
        waitQueue = []
        execute = 0
        idle = self.ctxt
        time = 0

        self.wait = sorted(self.data, key=method['ord'])
        print(f'\nEspera inicial: { self.wait}\n')
        
        while True:
            print(f'\n<------ time = {time} ------->')
            print(f'Current: {self.currentProcess}')
            column = []
            
            #setting of the col waitqueue
            for waiting in self.wait:
                if waiting.arrival == time:
                    waitQueue.append(waiting)
                    self.wait = self.rotateWait()
                    

            # Appending of process in excecution
            if self.currentProcess is None:
                column.append(('0', 0))
            else:
                column.append((self.currentProcess.name, self.currentProcess.remaining_time))

            # Appending of current waiting queue
            column.append([(p.name, p.remaining_time) for p in copy.deepcopy(waitQueue)])

            # Appending of column i in df
            df.append(column)

            # End of time i
            print(f'<------------------------------>')
            time += 1

            # Executing process if exists and checking if its done
            if self.currentProcess is not None and not self.currentProcess.done:
                self.checkFinish(self.currentProcess)

                self.currentProcess.remaining_time -= 1
                execute += 1
                print(f'Process ({self.currentProcess.name}, {self.currentProcess.remaining_time}) executed: {execute} times')
                if self.currentProcess.done:
                    print(f'Process {self.currentProcess.name} done: {self.currentProcess.done}')
                    self.currentProcess = None
                    execute= 0

                
                if execute == self.quantum and self.currentProcess is not None:
                    print(f'max execution time reached execute: {execute}, quantum: {self.quantum}')
                    execute = 0
                    waitQueue.append(self.currentProcess)
                    print(f'Current appended to wait queue {self.currentProcess.name}: {self.currentProcess.remaining_time}')
                    self.currentProcess = None
                    print(f'Current process to None')

            # If process awaiting and no current process, from waiting queue to execution queue
            if waitQueue and self.currentProcess is None:
                if idle == self.ctxt:
                    idle = 0
                    self.currentProcess = waitQueue.pop(0)
                    print(f'Current changed to: {self.currentProcess.name} remaining: {self.currentProcess.remaining_time}')
                else:
                    idle += 1
                    print(f'idle time: {idle}')

            # Checking if all process are done
            if self.isProcessingDone() :
                print('------------------------------------------------------------')
                print(f'\nProcessing with {method["name"]} done in time {time}')
                print(f'data before restart:\n {self.data}')
                self.restart()
                print(f'data after restart:\n {self.data}')
                print('------------------------------------------------------------')
                break
                
        return df
    
    def toDataFrame(self, l):
        d = {}
        print("prueba",l)
        for i in range(len(l)):
            aux = l[i][1]
            
            aux.insert(0,l[i][0])
            
            d[str(i)]=pd.Series(aux)
        df = pd.DataFrame(d)

        self.time_df= self.CreateDataTimes(df)

        df = df.transpose()
        json_df = df.to_json()
        
        return json_df
    
    def mean(self, dic):
        cont = 0
        for num in dic:
            cont+=dic[num]

        return round(cont/len(dic),4)

    def TimeReturn(self, df):
        time_return={}
        time_0 = True
        for col in df:
            for fila in df[col]:
                
                if not pd.isna(fila) :
                    for process in self.data:
                        
                        if str(fila[0])==process.name:
                            if not str(fila[0]) in time_return and time_0:
                                time_return[fila[0]] = 0
                            elif not str(fila[0]) in time_return and time_0!=True:
                                time_return[fila[0]] = 1
                            else:
                                time_return[fila[0]] += 1

            time_0 = False
               
                                
        time_tuplas=[]               
        for process in time_return:
            time_tuplas.append((process,time_return[process]))
        time_tuplas.append(("PROMEDIO",self.mean(time_return)))

        return time_tuplas 

    def TimeWait(self, df):
        time_wait = {}
        aux = df[1:]
        time_0 = True
            
        for col in aux:
                
            for fila in aux[col]:
                if not pd.isna(fila):
                    for process in self.data:
                        if str(fila[0])==process.name:
                            if not str(fila[0]) in time_wait and time_0:
                                time_wait[fila[0]] = 0
                            elif not str(fila[0]) in time_wait and time_0!=True:
                                time_wait[fila[0]] = 1
                            else:
                                time_wait[fila[0]] += 1

            time_0 = False                          
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

    


    

