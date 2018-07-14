# now building a new range class
class range_examp:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step 
            return return_val

# testing
# for i in range_examp(5):
    # print(i)

x = range_examp(5)
x.__next__()
next(x)

[print(i) for i in x]