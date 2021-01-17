
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
