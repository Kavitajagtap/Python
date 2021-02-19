
## 1.Write a Python program to count and display the vowels of a given text.

s1 = input("Enter any string = ")
count = 0
s = []
for i in s1:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            count=count+1
            s.append(i)
print("Number of vowels are = ",count)
print("vowels = ", s)

-------------------------------------------------------------------------------------------------------------------

## 2. Write a Python program to split a string on the last occurrence of the delimiter.

s1 = input("Enter any string = ")
print("original string = ",s1)
print("splited a string = ",s1.rsplit(',',1))

-------------------------------------------------------------------------------------------------------------------

## 3. Write a Python program to find the first non-repeating character in given string.

s = input("Enter a string = ")
s1 = [a for a in s if s.count(a) == 1]
print("First non-repeating character =",s1[0])

-------------------------------------------------------------------------------------------------------------------
