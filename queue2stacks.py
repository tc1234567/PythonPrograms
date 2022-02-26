
class Queue2Stacks(object):
    def __init__(self):
        
        self.instack = []
        self.outstack = []
        
    def enqueue(self, element):
        
        self.instack.append(element)

    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
                
        return self.outstack.pop()
    
    def peek(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
                
        print(self.outstack[-1])
        
        
        

instack = []
outstack = []

Q = Queue2Stacks()

q = int(input())

for i in range(q):
    user = input().split()
    if user[0] == str(1):
        Q.enqueue(user[1])
    if user[0] == str(2):
        Q.dequeue()
    if user[0] == str(3):
        Q.peek()
    
