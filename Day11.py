# 1.Write a  program to print all unique values in a dictionary.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    key = int(input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
print("unique values in a dictionary =",set(dict.values()))

---------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a  program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    key = int(input("key: "))
    value = eval(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
l1 = list(dict.values())
for i in l1[0]:
    for j in range(1, len(l1)):
        for a in l1[j]:
            dict1 = i + a
            print(dict1#
                  
-------------------------------------------------------------------------------------------------------------------------------------
                  
# 3.Write a  program to find the highest 3 values in a dictionary.
 dict = {}
n = int(input("Enter elements:"))
for i in range(n):
    key = (input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
list = sorted(set(dict.values()))
print("highest 3 values in dictionary =",set(list[-3:]))
                 
----------------------------------------------------------------------------------------------------------------------------------------                  
