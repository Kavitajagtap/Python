
# 1.Write a  program to check whether two lists are circularly identical.

a = eval(input("Enter list1 = "))
b = eval(input("Enter list2 = "))

if ' '.join(map(str, a)) in ' '.join(map(str, b * 2)):
    print("lists are circularly identical")
else:
    print("lists are not circularly identical")
 '''   
 Output:
 
  Enter list1 = [4,4,2,2,4]
  Enter list2 = [4,4,4,2,2]
  lists are circularly identical
'''
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
'''
Output:

Enter length of list:4
Enter element of list:
5
45
80
23
list = [5, 45, 80, 23]
second smallest number in a list = 23
'''
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
'''
Output:

Enter length of list:5
Enter element of list:
10
67
55
55
10
list = [10, 67, 55, 55, 10]
Unique values = [10, 67, 55]
'''
------------------------------------------------------------------------------------------------------------------
