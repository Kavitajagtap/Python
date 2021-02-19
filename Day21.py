
## 1 Write a Python program to count and display the vowels of a given text. 

s1 = input("Enter any string = ")
count = 0
s = []
for i in s1:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count=count+1
            s.append(i)
print("Number of vowels are = ",count)
print("vowels = ", s)

## 2. Write a Python program to count occurrences of a substring in a string.

string = input("Enter any string = ")
substring = input("Enter substring = ")
print("occurrence of substring in given string = ",string.count(substring))

## 3. Write a Python program to check if a string contains all letters of the alphabet

def check(s1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for n in alphabet:
        if n not in s1.lower():
            return False
    return True

s1 = input("Enter any string = ")
if (check(s1) == True):
    print("string contains all letters the of the alphabet")
else:
    print("string doesn't contains all the letters of the alphabet")
