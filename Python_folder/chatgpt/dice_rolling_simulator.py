import random

num_rolls = int(input("Enter the number of times to roll the dice: "))
for i in range(num_rolls):
    roll = random.randint(1, 6)
    print("Roll #{}: {}".format(i+1, roll))