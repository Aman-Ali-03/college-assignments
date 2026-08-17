# Write a Python program to remove: * specific key * last inserted item

# Display the dictionary after each operation.

dic = {
    'name':'Aman Ali',
    'roll no.':2507,
    'grade':'A',
    'section':'2A'
}

dic.pop('grade')
print(dic)

dic.popitem()
print(dic)