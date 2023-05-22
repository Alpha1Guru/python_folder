import random

num = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 1
while guess != num:
    if guess < num:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
print("You guessed it in {} tries!".format(tries))
