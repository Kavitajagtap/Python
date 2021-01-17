
# 1.Write a program to concatenate following dictionaries to create a new one.

def dict1():
 d = {}
 n = int(input("Enter elements of dictionary"))
 for i in range(n):
   key = int(input("key = "))
   value = int(input("value = "))
   d[key] = value
 return d
d1 = dict1()
d2 = dict1()
d3 = dict1()
print("dict1 =",d1,"\ndict2 =",d2,"\ndict3 =",d3)
dic4 = {}
for i in (d1, d2, d3):
    dic4.update(i)
print("Concatenated dictionary =",dic4)

# 2. Write a Program to check whether a given key already exists in a dictionary

dict = {}
n= int(input("Enter elements = "))
for i in range(n):
    key = int(input("key: "))
    value = int(input("value: "))
    dict[key] = value
print("Dictionary =",dict)
x = int(input("enter any key to check = "))
if x in dict:
    print('Key exist in the dictionary')
else:
    print('Key is not exist in the dictionary')

# 3. Write a Program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

n = int(input("Enter any number = "))
dict={key:key * key for key in range(1,n+1)}
print("Dictionary =",dict)

