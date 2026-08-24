str = input('Enter you Sentence: ')
list = str.split()
print(list)
print(max(list,key=len))