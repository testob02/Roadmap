class Fib:
    def __init__(self,limit):
        self.limit = limit
        self.counter = 1
        self.a = 0
        self.b = 1
        self.c = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.limit >= self.counter:
            self.c = self.a + self.b
            self.a = self.b
            self.b = self.c
            self.counter +=1
            return self.c
        else:
            raise StopIteration
        
fib = iter(Fib(5))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

