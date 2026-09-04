# Write a function count_vowels(text) that accepts a string and returns the number of
# vowels in it.

def count_vowels(text):
    return text.count('a')+text.count('e')+text.count('i')+text.count('o')+text.count('u')

sentence = input('Enter your Sentence: ')
print(f"Your sentence have {count_vowels(sentence)} vowels")