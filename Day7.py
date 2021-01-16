
# 1.Write a Python program to get the frequency of the elements in a list

l1 = eval(input("Enter list :"))
count = {}
for x in l1:
  if x in count:
     count[x] += 1
  else:
     count[x] = 1
print("frequency of a element in a list =\n",list(count.items()))
'''
Output:

Enter list :[10,'a',"abc",10,25,25,'a','a']
frequency of a element in a list =
 [(10, 2), ('a', 3), ('abc', 1), (25, 2)]

'''
-------------------------------------------------------------------------------------------

# 2.write a  program to count the number of elements in a list within a specified range.

list = eval(input("Enter list:"))
min = int(input("minimum:"))
max = int(input("maximum:"))
c = 0
for x in list:
 if min <= x <= max:
  c += 1
print("number of element within ",min,"to",max,"=",c)
'''
Output:

Enter list:[10,32,58,90,42,99,60,53,20]
minimum:50
maximum:100
number of element within  50 to 100 = 5

'''
---------------------------------------------------------------------------------

#3.Write a program to check whether a list contains a sublist.

list = eval(input("Enter list:"))
sublist = eval(input("Enter sublist:"))
c = 0
if set(sublist).issubset(set(list)):
    c = 1
if (c):
    print("list contains a sublist")
else:
    print("list doesn't contains a sublist")
'''
Output :

Enter list:[10,20,45,98,23,11]
Enter sublist:[20,45,98]
list contains a sublist

'''
