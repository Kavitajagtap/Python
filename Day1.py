# 1.Create List and Displayed with append() and without append() 

print("using append() method")
list = []
num = int(input("Enter length of a list: "))
print("Enter elements of list:")
for i in range(num):
 l1 = int(input())
 list.append(l1)
print("list =",list)

print("without using append() method")
l1 = eval(input("Enter list :"))
print("list =",l1)

'''
Output :-
using append() method

Enter length of a list: 4
Enter elements of list:
454
22
778
55

list = [454, 22, 778, 55]
without using append() method

Enter list :[10,'a',789,"abc",43]
list = [10, 'a', 789, 'abc', 43]
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Add element at first, last and specific location in list 

print("add element at first location")

list = eval(input("list ="))
list.insert(0,"Mango")
print(list)

print("add element at specific location")

list1 = eval(input("list1 ="))
list1.insert(2,"Mango")
print(list1)

print("add element at last location") 

list2 = eval(input("list2 ="))
list2.append("Mango")
print(list2)
'''
Output :-

add element at first location
list = ["Orange",'a',34,"$",23.4]
['Mango', 'Orange', 'a', 34, '$', 23.4]

add element at specific location
list1 = ["Orange",'a',34,"$",23.4]
['Orange', 'a', 'Mango', 34, '$', 23.4]

add element at last location
list2 =  ["Orange",'a',34,"$",23.4] 
['Orange', 'a', 34, '$', 23.4, 'Mango']

'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.Remove element from first position ,last position and specific position from list.

print("Remove element form first position -->")
l1 = eval(input("Enter list ="))
l1.remove(l1[0])
print(l1)

print("Remove element form specific position-->")
l2 = eval(input("Enter list ="))
l2.remove(l2[2])
print(l2)

print("Remove element form last position-->")
l3 = eval(input("Enter list ="))
l3.remove(l3[-1])
print(l3)

'''
Output :-
 
 Remove element form first position -->
Enter list = [11,34,"Kavita",54.9,'b',20] 
[34, 'Kavita', 54.9, 'b', 20]

Remove element form specific position-->
Enter list = [11,34,"Kavita",54.9,'b',20] 
[11, 34, 54.9, 'b', 20]

Remove element form last position-->
Enter list =  [11,34,"Kavita",54.9,'b',20]
[11, 34, 'Kavita', 54.9, 'b']
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 
