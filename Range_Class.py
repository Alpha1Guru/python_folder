class MyRange:
    def __init__(self, *args):
        num_args = len(args)
        if num_args == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif num_args == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif num_args == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        elif num_args > 3:
            raise TypeError(
                "MyRange expected at most 3 arguments, got {}".format(num_args))
        elif num_args == 0:
            raise TypeError("MyRange expected at least 1 arguments, got {}".format(num_args))

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += self.step

    def __len__(self):
        if self.step == 0:
            raise ValueError("MyRange() arg 3 must not be zero")
        print("(max(0, (self.stop - self.start + self.step - 1) // self.step)) ", max(0, (self.stop - self.start + self.step - 1) // self.step) )
        return max(0, (self.stop - self.start + self.step - 1) // self.step)
    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError("MyRange index out of range")
        print(f"self.start + index * self.step = {self.start} + {index} * {self.step} =", self.start + index * self.step)
        return self.start + index * self.step

# Test the custom MyRange class
my_range = MyRange(10, 6)

# print("range:\n", dir(range), "\n")
# print("MyRange: \n", dir(MyRange), "\n")

for i in my_range:
    print(i)

print("Index: ", my_range.__getitem__(5))
