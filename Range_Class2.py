class Range:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step
    
    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += self.step
    
    def __len__(self):
        return max(0, (self.end - self.start + self.step - 1) // self.step)
    
    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError("Range index out of range")
    
    def __repr__(self):
        return f"Range({self.start}, {self.end}, {self.step})"
