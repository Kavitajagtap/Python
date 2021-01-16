
# 1.Write a Python program to get the frequency of the elements in a list

l1 = eval(input("Enter list :"))
count = {}
for x in l1:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print("frequency of a element in a list =\n",list(count.items()))

# 2.write a  program to count the number of elements in a list within a specified range.

list = eval(input("Enter list:"))
min = int(input("minimum:"))
max = int(input("maximum:"))
c = 0
for x in list:
 if min <= x <= max:
  c += 1
print("number of element within ",min,"to",max,"=",c)

