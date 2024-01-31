def word_count(sentence: str):
    words = []
    word = ""
    # the algorithm only counts or add a word 
    #when a chunk 
    #of non whitespace characters are followed by 
    #a whitespace character therefore I add a
    #whitespace at the sentence so that the last
    # chunk of words can be counted 
    sentence +=  " "
    for char in sentence:
        if char not in (" ", "\n","\t"):
            word = word + char
        else:
            if word:
                words.append(word)
                word = ""
    return len(words)
if __name__ == "__main__":
    while True:
        print(f"Word Count: {word_count(input('Type Here: '))}")