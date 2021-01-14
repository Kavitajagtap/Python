# 1.Write a  program to generate all permutations of a list.

def per(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l =[]
    for i in range(len(lst)):
        a = lst[i]
        ab = lst[:i] + lst[i + 1:]
        for x in per(ab):
            l.append([a] + x)
    return l

l1 = eval(input("Enter list: "))
print("all permutations of a list:")
for p in per(l1):
    print(p)
'''
Output:
'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a  program to get the difference between the two lists.

l1 = [1,3,5,7,9]
l2 = [1,2,4,6,7,8]

a = list(set(l1) - set(l2))
b = list(set(l2) - set(l1))

diff = a + b
print("difference between list =",diff)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3.Write a  program to convert a list of characters into a string. 

s = eval(input("list of character: "))
s = ''.join(s)
print("string =",s)

