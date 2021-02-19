
## 1.Write a  program to find the first repeated word in a given string.

def check(s1):
  temp = set()
  for word in s1.split():
    if word in temp:
      return word
    else:
      temp.add(word)
  return 'None'
print("First repeated word in a given string = ",check(input("Enter a string: ")))

----------------------------------------------------------------------------------------

## 3.Write a program to remove spaces from a given string

s1 = input("Enter a string which contains spaces: ")
s1 = s1.replace(' ', '')
print("string after removing spaces = ",s1)

------------------------------------------------------------------------------------------
