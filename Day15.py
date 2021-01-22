
# 1. Write a program to print a dictionary line by line.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("dictionary = ",dict,"\nDictionary line by line: ")
for k,v in dict.items():
    print(k)
    print(v)
