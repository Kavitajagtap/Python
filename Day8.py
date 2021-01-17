
# 1.Write a program to create dictionary and access all elements with keys and values

dict = eval(input("Enter dictionary = "))
print("Accessing Elements from dictionary -->")
for key in dict:
    print(key,dict[key])
'''
Output :

Enter dictionary = {'Apple':2017,'Microsoft':1985,'Facebook':2012,'Amazon':1997}
Accessing Elements from dictionary -->
Apple 2017
Microsoft 1985
Facebook 2012
Amazon 1997
'''
--------------------------------------------------------------------------------------
# 2.Write a Program to sort (ascending and descending) a dictionary by value.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("dictionary =",dict)
print("sorted dictionary in ascending order =",sorted(dict.items(), key=lambda x: x[1]))
print("sorted dictionary in descending order =",sorted(dict.items(), key=lambda x: x[1],reverse = True))
'''
Output:

Enter elements: 4
key: a
value: 4
key: b
value: 1
key: c
value: 6
key: d
value: 3
dictionary = {'a': 4, 'b': 1, 'c': 6, 'd': 3}
sorted dictionary in ascending order = [('b', 1), ('d', 3), ('a', 4), ('c', 6)]
sorted dictionary in descending order = [('c', 6), ('a', 4), ('d', 3), ('b', 1)]
'''
------------------------------------------------------------------------------------------------------

# 3.Write a Program to add a key to a dictionary.

dict = eval(input("Enter dictionary:"))
print("Your dictionary =",dict)
key = input("key: ")
value = int(input("value: "))
dict.update({key:value})
print("updated dictionary =",dict)
'''
Output:

Enter dictionary:{'Apple':2017,'Microsoft':1985,'Facebook':2012}
Your dictionary = {'Apple': 2017, 'Microsoft': 1985, 'Facebook': 2012}
key: Amazon
value: 1997
updated dictionary = {'Apple': 2017, 'Microsoft': 1985, 'Facebook': 2012, 'Amazon': 1997}
'''
-------------------------------------------------------------------------------------------------
