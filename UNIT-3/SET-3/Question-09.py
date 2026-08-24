str = input('Enter your String: ')
list = str.split()
for i in list :
    print(i[::-1],end=' ')