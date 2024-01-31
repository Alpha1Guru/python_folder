def word_count(sentence: str):
   return len(sentence.strip().split())
if __name__ == "__main__":
    while True:
        print(f"Word Count: {word_count(input('Type Here: '))}")