# Input a sentence and a word.
# - Check whether the word is present in the sentence
# using the in operator.

sen = input("Enter your sentence: ")
word = input("Enter word: ")

if word in sen:
    print("Sentence have the word.")
else:
    print("Sentence haven't this word.")