"""
 1.Write a program to sort a list alphabetically in a dictionary
Enter dictionary = {1: ['B', 'C', 'A'], 2: ['D', 'B', 'A'], 3: ['V', 'A', 'K']}
Sorted list of dictionary = {1: ['A', 'B', 'C'], 2: ['A', 'B', 'D'], 3: ['A', 'K', 'V']}

"""
dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = int(input("key: "))
    v = eval(input("value: "))
    dict[k] = v
print("Dictionary =",dict)

new_dict = {k: sorted(v) for k, v in dict.items()}
print("Sorted list of dictionary =",new_dict)

------------------------------------------------------------------------------------------------------------

"""
2.Write a program to remove spaces from dictionary keys
Dictionary = {'a b c': 15, 'd e f': 30, 'g h i': 45}
new dictionary = {'abc': 15, 'def': 30, 'ghi': 45}

"""
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

--------------------------------------------------------------------------------------------------------------

"""
3.Write a program to get the key, value and item in a dictionary.
Dictionary = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
key: a value: 10 item: ('a', 10)
key: b value: 20 item: ('b', 20)
key: c value: 30 item: ('c', 30)
key: d value: 40 item: ('d', 40)

"""
dict = {}
n = int(input("Enter elements: "))

for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("Dictionary =",dict)

for k, v in dict.items():
    print('key:', k, 'value:', v, 'item:', (k, v))
    
----------------------------------------------------------------------------------------------------------------
    
