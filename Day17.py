"""
1. Write a program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y

"""
def dict1():
 d = {}
 n = int(input("Enter elements of dictionary: "))
 for i in range(n):
   key = (input("key: "))
   value = int(input("value: "))
   d[key] = value
 return d
d1 = dict1()
d2 = dict1()
print("dict1 =",d1,"\ndict2 =",d2)

for (key, value) in (d1.items() & d2.items()):
    print('{}:'.format(key), value,'is present in both lists')
  
------------------------------------------------------------------------------------------------------------
  
"""
2. Write program to drop empty items from a given dictionary. 
Original dictionary :
{'c1':'Red','c2':'Pink','c3':None}
Output :
{'c1':'Red','c2':'Pink'}

"""
dict = eval(input("Enter dictionary = "))
print("Original dictionary =",dict)
dict = {k:v for (k, v) in dict.items() if v is not None}
print("Dictionary after dropping empty items:",dict)


"""
3.Write a program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key 
from the dictionary.

"""
d = {}
n = int(input("Enter elements of dictionary: "))
for i in range(n):
   k = (input("key: "))
   v = eval(input("value: "))
   d[k] = v
print("\nDictionary =",d,"\nfifth value of each key: ")
print(d["x"][4])
print(d["y"][4])
print(d["z"][4])

