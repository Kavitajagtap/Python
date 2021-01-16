
# 1.Write a Python program to get the frequency of the elements in a list

l1 = eval(input("Enter list :"))
count = {}
for x in l1:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
print("frequency of a element in a list =\n",list(count.items()))

