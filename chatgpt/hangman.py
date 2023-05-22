import random
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew", "indigo", "jujube", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon", "xigua", "yellow watermelon", "zucchini"]

word = random.choice(words)
letters_guessed = set()
max_guesses = 7
num_guesses = 0

while num_guesses < max_guesses:
    guess = input("Guess a letter: ")
    if guess in letters_guessed:
        print("You already guessed that letter.")
    else:
        letters_guessed.add(guess)
        if guess in word:
            print("Good guess!")
            if set(word) == letters_guessed:
                print("Congratulations, you won! The word was {}".format(word))
                break
        else:
            print("Sorry, that letter is not in the word.")
            num_guesses += 1
            print("You have {} guesses left.".format(max_guesses - num_guesses))

if num_guesses == max_guesses:
    print("Sorry, you lost. The word was {}.".format(word))
