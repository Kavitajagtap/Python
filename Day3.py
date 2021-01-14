
# 1.Write a  program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list = []
n = int(input("length of a list:"))
print("Enter elements of list:")
count = 0
for i in range(n):
    l1 = (input())
    list += [l1]
    if len(l1) > 1 and l1[0] == l1[-1]:
        count = count + 1
print("list =",list)
print("number of strings having same first and last character in a list = ",count)

'''
Output:
length of a list:5
Enter elements of list:
abc
xyz
aba
1221
414
list = ['abc', 'xyz', 'aba', '1221', '414']
number of strings having same first and last character in a list =  3
'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 

def last(n):
    return n[-1]
def sorted_list(tuples):
    return sorted(tuples, key=last)

list = []
l1 = ((input("Enter the list of tuples:\n")))
while (l1 != ''):
    list.append(tuple(map(int, l1.split())))
    l1 = input()
print("list =",list)
print("Sorted list =",sorted_list(list))

'''
Output :
Enter the list of tuples:
2 5
1 2
4 4
2 3
2 1

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Sorted list = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3.Write a  program to remove duplicates elements from a list.

list1 = []
num = int(input("length of a list:"))
print("Enter elements of list:")
for i in range(num):
 list1.append(int(input()))
print("list = ", list1)
Newlist = list(set(list1))
print("list without duplicates:",Newlist) 

'''
Output :
length of a list:6
Enter elements of list:
10
20
50
60
50
20
list =  [10, 20, 50, 60, 50, 20]
list without duplicates: [10, 20, 50, 60
]'''

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

