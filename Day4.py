
# 1.Write a program to check a list is empty or not. 

list = []
num = int(input("length of a list:"))
print("Enter elements of list:")
for i in range(num):
    list.append((input()))
print("list =",list)
if len(list) == 0:
    print("list is empty")
else:
   print("list is not empty")
'''
Output:
length of a list:0
Enter elements of list:
list = []
list is empty'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a  program to find the list of words that are longer than n from a given list of words. 

s1 = input("Enter any strings =")
a=s1.split(" ")
n=int(input("enter value of n ="))
list = [i for i in a if len(i) > n]
print("list of words =",list)
'''
Output:-
Enter any strings =Hello I am Kavita Vijay Jagtap
enter value of n =3 
list of words = ['Hello', 'Kavita', 'Vijay', 'Jagtap']
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3.Write a program to print the numbers of a specified list after removing even numbers from it.

list = []
list = eval(input("Enter list: "))
list = [a for a in list if a%2 != 0]
print("list after removing even numbers from it =",list)
'''
output :-

Enter list: [10,45,90,33,67,78,55]
list after removing even numbers from it = [45, 33, 67, 55]
'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
