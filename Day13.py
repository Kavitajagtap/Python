
## 1.Write a program to print a dictionary in table format

dict = {}
n = int(input("Enter elements of dictionary: "))
for i in range(n):
    key = input("key: ")
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict,"\nDictionary in table format:")
print('{:10} {}'.format('COMPANY', 'YEAR'))
for key in dict:
    print('{:10} {} '.format(key, dict[key]))
 
--------------------------------------------------------------------------------------------------------------------------------------------------------

"""
2. Write a  program to count the values associated with key in a dictionary. 
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
"""

list = eval(input("list of Dictionaries:\n"))
count = 0
for dict in list:
    if 'success' in dict:
        if dict['success'] == True:
             count += 1
print("count of success true =",count)

--------------------------------------------------------------------------------------------------------------------------------------------------------

## 3. Write a program to convert a list into a nested dictionary of keys
list = []
n = int(input("length of a list:"))
print("elements of list:")
for i in range(n):
    list.append(int(input()))
print("list =",list)
dict = c = {}
for i in list:
    c[i] = {}
    c = c[i]
print("Nested dictionary of key:",dict)

--------------------------------------------------------------------------------------------------------------------------------------------------------
