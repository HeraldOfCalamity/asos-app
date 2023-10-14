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
        elif self.method == 'PRIO_sm' or self.method == 'PRIO_gt':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.priority})
        elif self.method == 'SJF':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.cpu_time})
        elif self.method == 'SRT':
            solution = self.baseAlgorithm({'name':self.method, 'ord':lambda process: process.arrival})
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
            
            # To set first waiting queue if prio or sjf
            # if time == 0 and (method['name'][0:4] == 'PRIO' or method['name'] == 'SJF'):
            #     waitQueue = self.data

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

