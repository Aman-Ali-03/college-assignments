# Build a program that reports: 
#  · number of lines 
# . number of words 
# . number of characters 
# · number of blank lines 
# . number of occurrences of a user-specified word

word = input("Enter your word.")
lines = 0
words = 0
num_char = 0
blank_line = 0
occur_word = 0

with open("Challenge-03.txt","r") as read_from:
    for i in read_from:
        lines += 1
        splited = i.split()
        words += len(splited)
        num_char += len(i)
        if len(i)<2:
            blank_line += 1
        occur_word += i.count(word)

print(f"Lines = {lines}")
print(f"Words = {words}")
print(f"Num of character = {num_char}")
print(f"Number of blank line = {blank_line}")
print(f"Occurense of {word} = {occur_word}")