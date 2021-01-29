"""
1. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

"""
words = input("sequence of words:")
temp = [i for i in words.split(",")]
print("unique words in sorted form =",",".join(sorted(list(set(temp)))))

## 2. Write a program to insert a string in the middle.
