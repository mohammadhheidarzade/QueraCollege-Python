class Reverse:

    def __init__(self, ls):
        self.ls = ls[::-1]
        self.i = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i + 1 >= len(self.ls):
            raise StopIteration
        self.i += 1
        return self.ls[self.i]