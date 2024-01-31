import string
def word_count(sentence: str):
   count = 0
   # Get the index of the first non whitespace 
   for i in range(len(sentence)):
       if sentence[i] not in string.whitespace:
           first_non_whitespace = i
           break
   #Get the index of the last non whitespace
   for i in range(len(sentence)-1, -1,-1):
       if sentence[i] not in string.whitespace:
           last_non_whitespace = i
           break
   #Loop within the two boundaries 
   for i in range(first_non_whitespace, last_non_whitespace +1):
       #Check for a whitespace
       if sentence[i] in string.whitespace:
           #if there is adjacent whitespace after it then ignore
           if sentence[i+1] in string.whitespace:
               continue
           # else count this whitespace
           elif sentence[i+1] not in string.whitespace:
               count += 1
   return count + 1 # add one to it to get the number of words
if __name__ == "__main__":
    while True:
        print(f"Word Count: {word_count(input('Type Here: '))}")