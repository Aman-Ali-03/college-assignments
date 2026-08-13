# 6. Input a sentence and a word.
# - Check whether the word is not present in the
# sentence.

sen = input("Enter your sentence: ")
word = input("Enter word: ")

if word not  in sen:
    print("Sentence haven't the word.")
else:
    print("Sentence have this word.")