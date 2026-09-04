# Write a Python program to create a dictionary from the following two lists.

# keys = ["ID","Name","Age","City"]
# values = [101,"Ankit",20,"Delhi"]
# Expected Output: {'ID':101,'Name':'Ankit','Age':20,'City':'Delhi’}

keys = ["ID","Name","Age","City"]
values = [101,"Ankit",20,"Delhi"]

# dic = {}
# for i in range(0,len(keys)):
#     dic[keys[i]] = values[i]

dic = dict(zip(keys,values))

print(dic)