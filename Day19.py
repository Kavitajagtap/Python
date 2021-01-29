## 1.Write a Python function that takes a list of words and returns the longest word and the length of the longest one.
 def long_word(list):
    length = []
    for i in list:
        length.append((len(i), i))
    length.sort()
    return length[-1][0], length[-1][1]

list = []
n = int(input("length of a list = "))
print("elements of list:")
for i in range(n):
    list.append(input())
print("list =",list)

a = long_word(list)
print("Longest word =",a[1])
print("Length of the longest word =",a[0])
