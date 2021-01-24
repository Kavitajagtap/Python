
"""
1. Write program to sort Counter by value. 
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

"""
dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("dictionary = ",dict)
print("Dictionary sorted by value = ")
print(sorted(dict.items(), key=lambda x: x[1], reverse=True))

## 2.  Write a program to create a dictionary from two lists without losing duplicate values.

l1 = []
num = int(input("First list\nlength of a list:"))
print("Enter elements of list:")
for i in range(num):
    l1.append((input()))

l2 = []
num = int(input("Second list\nlength of a list:"))
print("Enter elements of list:")
for i in range(num):
    l2.append(int(input()))

d = {l1[i]: l2[i] for i in range(len(l1))}
print("dictionary =",d)

## 3. Write a program to replace dictionary values with their average.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = eval(input("value: "))
    dict[k] = v
print("dictionary = ",dict)
d1 = {k:sum(v)/len(v) for k, v in dict.items()}
print("New dictionary =",d1)
