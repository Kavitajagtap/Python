"""
1.Write a Python program to combine values in python list of dictionaries. Go to the editor
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
"""
d1 = eval(input("Enter dict1:"))
d2 = eval(input("Enter dict1:"))
d3 = eval(input("Enter dict1:"))
l1 = [d1,d2,d3]
print("list of dictionaries =",l1)

list = []
for d in l1:
    list.append(tuple(d.values()))
dict = {}
for i in list:
    if i[0] in dict:
        dict[i[0]] += i[1]
    else:
        dict[i[0]] = i[1]
print("new dictionary =",dict)



