import random
class Myclass():
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = Myclass()
myinst.dothis()
print(myinst.rand_val)