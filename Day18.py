"""
1. Write a  program to count the number of characters (character frequency) in a string
Sample String : ‘google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
s1 = input("Enter any string = ")
count = {}
for x in s1:
    if x in count.keys():
        count[x] += 1
    else:
        count[x] = 1
print("count of the characters =",count)
