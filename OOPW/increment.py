#Procedural paradigm
def increment(arg):
    arg = arg + 1;
    return arg;

#Object paradigm
class MyCustomInt:
    def __init__(self):
        self.val = 0
    def increment(self):
        self.val = self.val + 1
    def __repr__(self):
        return str(self.val)
if __name__ == "__main__":
    # Procedural paradigm
    something = 0
    something = increment(something)
    print(something)
    
    # Object paradigm
    this = MyCustomInt()
    this.increment()
    print(this)