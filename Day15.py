
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
    
-----------------------------------------------------------------------------------------------------------------------

 # 2. Write a program to check multiple keys exists in a dictionary.

while 1:
    dict = {}
    n = int(input("Enter elements: "))
    for i in range(n):
        k = (input("key: "))
        v = int(input("value: "))
        dict[k] = v
    print("dictionary = ",dict)
    if len(dict.keys()) > 1:
        print("multiple keys exists in a dictionary")
    else:
        print("multiple keys doesn't exists in a dictionary")

-----------------------------------------------------------------------------------------------------------------------

# 3. Write a program to count number of items in a dictionary value that is a list.

dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = eval(input("value: "))
    dict[k] = v
print("dictionary = ",dict)
for k, v in dict.items():
    if isinstance(v, list):
        print('key=', k, 'lenth of value=', len(v))
    else:
        print('key=', k, 'value is not a list')
