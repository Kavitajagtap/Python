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

# 
