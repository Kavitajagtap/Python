# 1.Write a program to sort a list alphabetically in a dictionary.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = int(input("key: "))
    v = eval(input("value: "))
    dict[k] = v
print("Dictionary =",dict)
new_dict = {k: sorted(v) for k, v in dict.items()}

print("Sorted list of dictionary =",new_dict)

# 2.Write a program to remove spaces from dictionary keys.
dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("Dictionary =",dict)
for key in dict:
    k1 = key.replace(' ', '')
    dict[k1] = dict.pop(key)
print("new dictionary =",dict)

# 3.Write a program to get the key, value and item in a dictionary.
dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("Dictionary =",dict)
for k, v in dict.items():
    print('key:', k, 'value:', v, 'item:', (k, v))
