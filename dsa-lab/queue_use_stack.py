class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop_st(self) -> int:
        if not self.st2 and self.st1:
            while self.st1:
                self.st2.append(self.st1.pop())
          
        if self.empty():
            return True

        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2 and self.st1:
            while self.st1:
                self.st2.append(self.st1.pop()) 
        
        if not self.st2:
            return True
            
        return self.st2[-1]
        

    def empty(self) -> bool:
        if not self.st2 and self.st1:
            while self.st1:
                self.st2.append(self.st1.pop())
                
            return False
        
        if not self.st2:
            return True
        
        return False
