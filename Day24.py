
## 2.Write a Python program to find the first repeated character in a given string. 

s1 = input("Enter a string = ")
dict = []
for n in s1:
    if n in dict:
        print("first repeated character = ",n)
        break
    else:
        dict.append(n)
if dict == list(s1):
    print("no repeated character present in the string.")
'''
output :-
Enter a string = adsads
first repeated character =  a
'''
----------------------------------------------------------------------------------------------

## 3.Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest.

s1 = input("Enter a string = ")
dict = []
for n in s1:
    if n in dict:
        print("first repeated character = ",n,",",s1.index(n))
        break
    else:
        dict.append(n)
if dict == list(s1):
    print("no repeated character present in the string.")
'''
Output :
Enter a string = abcxxy
first repeated character =  x , 3
'''
