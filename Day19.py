
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

-------------------------------------------------------------------------------------------------------

## 2. Write a Python program to remove the nth index character from a nonempty string.
def rem(s1, n):
    a = s1[:n]
    b = s1[n + 1:]
    return a + b

s1 = input("Enter any string = ")
n = int(input("Enter nth index character to remove = "))
print("New string: ",rem(s1, n))

## 3.Write a Python program to remove the characters which have odd index values of a given string. 
def oddval(s1):
  s2 = ""
  for i in range(len(s1)):
    if i % 2 == 0:
      s2 = s2 + s1[i]
  return s2
s1 = input("Enter any string = ")
print("string after removing odd index characters =",oddval(s1))
