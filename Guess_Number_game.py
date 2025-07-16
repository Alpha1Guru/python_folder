#A guessing game
import random
print("Welcome To Guess A Number Game")
run = True
while run:
    message = "I am thinking of a whole number. What do you think it is?"
    thought_number = random.randint(1, 100)
    guessed_number = int(input(f"{message}: "))

    while guessed_number != thought_number:
        if guessed_number < thought_number:
            message = f"{guessed_number} is too LOW!\tTry again!"
            guessed_number = int(input(f"{message}: "))
        else:
            message = f"{guessed_number} is too HIGH!\tTry again!"
            guessed_number = int(input(f"{message}: "))
    print("Congratulations! You guess matches my thought!")

    run_again = input("Do you want to play again? (yes/no): ")
    if run_again != "yes":
        print("Thanks for playing. See you next time😊")
        run = False