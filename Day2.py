
# 1.Write a Python program to create an list without append()  display the list items. Access individual element through indexes.

list = eval(input("Enter list: "))
print("list =",list)
print("display list items:-->")
for i in list:
    print(i)
print("Access individual element of list through indexes:-->")
for i in range(len(list)):
    print(list[i])
    
'''
Output :
Enter list: [123,'a',56,78,"abc"]
list = [123, 'a', 56, 78, 'abc']
display list items:-->
123
a
56
78
abc
Access individual element of list through indexes:-->
123
a
56
78
abc
'''
--------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a program to get the number of occurrences of a specified element in an list.

def count(list, x):
    c= 0
    for i in list:
        if (i == x):
            c = c + 1
    return c
list = eval(input("Enter list: "))
print("list =",list)
x = int(input("Enter specific element which is present in the list:"))
print("{} occurred {} times in a list".format(x, count(list, x)))

'''
Output :
Enter list: [23,'a',43,"abc",43,78,21,43]
list = [23, 'a', 43, 'abc', 43, 78, 21, 43]
Enter specific element which is present in the list:43
43 occurred 3 times in a list
'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3 Write a program to remove the first occurrence of a specified element from  list.

list = eval(input("Enter list: "))
print("list =",list)
x = int(input("Enter specific element: "))
print("Remove the first occurrence of a specified element from list:")
list.remove(x)
print("New list = ",list)

'''
Output :-
Enter list: [90,67,'a',123,67,"abc",54,67]
list = [90, 67, 'a', 123, 67, 'abc', 54, 67]
Enter specific element: 67
Remove the first occurrence of a specified element from list:
New list =  [90, 'a', 123, 67, 'abc', 54, 67]
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------

