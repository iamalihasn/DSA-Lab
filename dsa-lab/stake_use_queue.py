class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q2 and self.q1:
            while self.q1:
                for _ in range(len(self.q1)-1):
                    self.q1.append(self.q1.pop(0))
                
                self.q2.append(self.q1.pop(0))
        
        if self.q1:
            while self.q1:
                self.q2.insert(0,self.q1.pop(0))
        
        if not self.q2:
            return True
        
        return self.q2.pop(0)




    def top(self) -> int:
        if not self.q2 and self.q1:
            while self.q1:
                for _ in range(len(self.q1)-1):
                    self.q1.append(self.q1.pop(0))
                
                self.q2.append(self.q1.pop(0))
        
        if self.q1:
            while self.q1:
                self.q2.insert(0,self.q1.pop(0))
        
        if not self.q2:
            return True
        
        return self.q2[0]

    def empty(self) -> bool:
        return not self.q1 and not self.q2
    

s = MyStack()
s.push(1)
s.push(2)
print(s.top())  # Should print 2
print(s.pop())  # Should print 2
print(s.empty())  # Should print False