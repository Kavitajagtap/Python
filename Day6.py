
# 1.Write a  program to check whether two lists are circularly identical.

a = eval(input("Enter list1 = "))
b = eval(input("Enter list2 = "))

if ' '.join(map(str, a)) in ' '.join(map(str, b * 2)):
    print("lists are circularly identical")
else:
    print("lists are not circularly identical")
------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a  program to find the second smallest number in a list.

list = []
n1=int(input("Enter length of list:"))
print("Enter element of list:")
for i in range(n1):
   k=int(input())
   list.append(k)
print("list =",list)
list.sort()
print("second smallest number in a list =",list[1])

---------------------------------------------------------------------------------------------------------------------------------

#3 3.Write a program to get unique values from a list

list1 = []
n1=int(input("Enter length of list:"))
print("Enter element of list:")
for i in range(n1):
   l = int(input())
   list1.append(l)
print("list =",list1)
print("Unique values =",list(set(list1)))

