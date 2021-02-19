
## There are 3 teacher's in college.  Every teacher teaches group of 3 subjects. You have to print common subject and unique subject 

def list1():
    l1 = []
    n1 = int(input("Enter number of subject:"))
    for i in range(n1):
        k = (input())
        l1.append(k)
    return l1

def common(teacher1,teacher2,teacher3):
    s1 = set(teacher1)
    s2 = set(teacher2)
    s3 = set(teacher3)
    set1 = s1.intersection(s2)
    res = set1.intersection(s3)
    for i in list(res):
        print(i)

def unique(teacher1,teacher2,teache3):
    a = teacher1 + teacher2 + teacher3
    for i in list(sorted(list(set(a)))):
        print(i)

teacher1 = list1()
teacher2 = list1()
teacher3 = list1()

unique(teacher1, teacher2, teacher3)
common(teacher1, teacher2, teacher3)

"""
input:
Enter number of subject:3
Python
C
Cpp
Enter number of subject:3
JAVA
C
Cpp
Enter number of subject:3
C
DBMS
Os

Output:

C
Cpp
DBMS
JAVA
Os
Python
C
"""
