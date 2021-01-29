"""
1. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

"""
words = input("sequence of words:")
temp = [i for i in words.split(",")]
print("unique words in sorted form =",",".join(sorted(list(set(temp)))))

----------------------------------------------------------------------------------------------------------------------------------------------------------------

## 2. Write a program to insert a string in the middle.
s1 = input("Enter any string = ")
s2 = input("enter a string to insert in the middle = ")
n = 6
res = s1[:n] + " " + s2 + " " + s1[n:]
print("New string = " + res)

## 3. Write a program to reverse words in a string.
def rev_string(s1):
   words = s1.split(' ')
   s2 = ' '.join(reversed(words))
   return s2

s1 = input("Enter any string = ")
print("String with reversing words =",rev_string(s1))

