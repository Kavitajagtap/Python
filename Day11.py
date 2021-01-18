# 1.Write a  program to print all unique values in a dictionary.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    key = int(input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
print("unique values in a dictionary =",set(dict.values()))
