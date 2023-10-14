from Process import ProcessItem
from typing import List
from Process import ProcessItem
import copy

class ProcessManagement:
    def __init__(self, data: List[ProcessItem], method: str) -> None:
        self.data = data
        self.method = method
        self.wait = None
        self.currentProcess = None  # al finalizar proceso reiniciar

    
    def generateGantt(self, method: str = None) -> list:
        solution = None

        # To change method
        if method:
            self.method = method

        if self.method == 'FCFS':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.arrival})
        elif self.method == 'RR':
            solution = self.RoudRobin()
        elif self.method[0:4] == 'PRIO':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.priority})
        elif self.method == 'SJF':
            solution = self.SJF()
        elif self.method == 'SRT':
            solution = self.SRT()
        else:
            solution = [f'-- Error: method {self.method} does not exist --']
        
        return solution
        
                
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
        else:
            self.wait = sorted(self.data, key=method['ord'])

        print(f'\nEspera inicial: { self.wait}\n')
        
        while True:
            print(f'\n<------ time = {time} ------->')
            print(f'Current: {self.currentProcess}')
            column = []
            
            #setting the col wait queue
            
            if method['name'] == 'FCFS':
                for waiting in self.wait:
                    if waiting.arrival == time:
                        waitQueue.append(waiting)
                        self.wait = self.rotateWait()

            elif method['name'][0:4] == 'PRIO':
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


    def RoudRobin(self, quantum: int = 1, ctxt: int = 1):
        pass

    def SRT(self, ctxt: int = 0):  # Shortest Remaining Time
        df = []
        time = 0
        end = False

        while True:
            print(f'<=========================>\n - Time: {time} -')
            col = []

            self.proToWait(time)
            currentWait = copy.deepcopy(self.wait)

            


            if self.wait and (self.currentProcess[1] == 1 or self.currentProcess[1] == 0):
                self.currentProcess = self.wait.pop(0)
            elif self.currentProcess[1] > 1:
                self.currentProcess = (self.currentProcess[0], self.currentProcess[1] - 1)

            

            # if currentWait and currentWait[0][1] < self.currentProcess[1]:
            #     print(f'En espera: {currentWait[0][1]}, currentProcess: {self.currentProcess[1]}, time: {time}')
            #     aux = self.currentProcess
            #     self.currentProcess = self.wait.pop(0)
            #     print(f'aux = {aux}, current: {self.currentProcess}')
            #     currentWait.append(aux)

            # print(f'currentProcess: {self.currentProcess}')
  
            
            # Excecution Zone
            print(f'currentWait: {currentWait}')
            if currentWait:
                end = False
                print(f'currentWait: {currentWait}')
            else:
                print('============== ending ==============')
                end = True
    




            col.append(self.currentProcess)
            if currentWait and col[0] == currentWait[0]:
                currentWait.pop()
            # Wait queue Zone
            col.append(currentWait)


            

            # Column appending Zone
            df.append(col)
            print('<=========================>')
            time += 1





            
            if self.currentProcess[1] == 1 and end:
                break
            
        return df

