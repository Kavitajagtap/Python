"""
1. Write program to sort Counter by value. 
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
dict = {}
n = int(input("Enter elements: "))
for i in range(n):
    k = (input("key: "))
    v = int(input("value: "))
    dict[k] = v
print("dictionary = ",dict)
print("Dictionary sorted by value = ")
print(sorted(dict.items(), key=lambda x: x[1], reverse=True))

