class Number_it():
    def __init__(self,n):
        self.begin=1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        val = self.begin
        if self.begin <= self.max:
            val = self.begin
            self.begin += 1
            return val
        else:
            raise StopIteration

def generator(n):
    s=1
    while s <= n:
        sq=s
        yield s
        s +=1










