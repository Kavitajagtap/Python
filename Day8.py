
# 1.Write a program to create dictionary and access all elements with keys and values

dict = eval(input("Enter dictionary = "))
print("Accessing Elements from dictionary -->")
for key in dict:
    print(key,dict[key])

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


