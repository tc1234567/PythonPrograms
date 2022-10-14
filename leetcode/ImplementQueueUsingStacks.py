class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)

    def pop(self) -> int:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1.pop()
        
    def peek(self) -> int:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return self.stack1[-1]
       
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
