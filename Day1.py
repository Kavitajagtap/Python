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
list1 = []
for i in range(num):
 l2 = int(input())
 list1.insert(i,l2)
print("list1 =",list1)
'''using append() method
Enter length of a list: 4
Enter elements of list:
454
22
778
55
list = [454, 22, 778, 55]
without using append() method
Enter length of a list: 4
Enter elements of list:
454
22
778
55
list = [454, 22, 778, 55]'''
