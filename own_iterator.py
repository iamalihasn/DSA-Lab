class OwnIterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration


class OwnIterable:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return OwnIterator(self.start,self.end)


own_iter = OwnIterable(1, 10)
for num in own_iter:
    print(num)

for num in own_iter:
    print(num)