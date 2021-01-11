
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

Output:
length of a list:0
Enter elements of list:
list = []
list is empty

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
