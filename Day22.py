
## 1.Write a Python program to convert a string in a list.

def Convert(string):
    l1 = list(string.split(" "))
    return l1

str1 = input("Enter a string = ")
print("Conversion of string to List = ",Convert(str1))

----------------------------------------------------------------------------------------

## 2. Write a Python program to lowercase first n characters in a string.

s1 = input("Enter a string = ")
n = int(input("Enter Number of character = "))
print("Updated string = ",s1[:n].lower() + s1[n:])

-----------------------------------------------------------------------------------------
"""
3. Write a Python program to swap comma and dot in a string. 

Sample string: "32.054,23"
Expected Output: "32,054.23"
"""
s1 = input("Enter a string which contains ',' &'.' = ")
temp = []

for i in range(len(s1)):
    if s1[i] == ".":
        temp.append(",")
    elif s1[i] == ",":
        temp.append(".")
    else:
        temp.append(s1[i])
print("after swapping string = ","".join(temp))

-----------------------------------------------------------------------------------------
