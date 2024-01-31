def word_count(sentence: str):
    words = []
    word = ""
    for i in range(len(sentence)):
        if sentence[i] not in (" ", "\n","\t") and i != len(sentence) -1:
            word = word + sentence[i]
        else:
            if word:
                words.append(word)
                word = ""
    return len(words)
if __name__ == "__main__":
    while True:
        print(f"Word Count: {word_count(input('Type Here: '))}")