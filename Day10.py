# 1.Write a program to remove a key from a dictionary.

dict = {}
n= int(input("Enter elements ="))
for i in range(n):
    key = int(input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
s = int(input("Enter any key to remove: "))
if s in dict:
  del dict[s]
print("Updated dictionary =",dict)

----------------------------------------------------------------------------

# 2. Write a  program to multiply all the items in a dictionary.

dict = {}
n= int(input("Enter elements ="))
for i in range(n):
    key = (input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
d = 1
for i in dict:
    d = d * dict[i]
print("Multiplication of all elements in dictionary =",d)

----------------------------------------------------------------------------

# 3. Write a  program to map two lists into a dictionary. 
def list():
 l1 = []
 n = int(input("Enter length of a list: "))
 print("Enter elements of list:")
 for i in range(n):
    l1.append(int(input()))
 return l1
a = list()
b = list()
print("list1 =",a,"\nlist2 =",b)
dict = {a[i]: b[i] for i in range(len(a))}
print("Mapping of two list in dictionary =",dict)

