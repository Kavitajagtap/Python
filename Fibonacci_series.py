
## Fibonacci series using for loop

n = int(input("Enter number of terms: "))
n1, n2 = 0, 1 # first two terms of fibonacci series

if n <= 0:
  print("Please enter a positive integer")
elif n == 1:
  print("Fibonacci sequence upto",n,":")
  print(n1)
else:
  print("Fibonacci sequence:")
  for i in range(n):
      print(n1,end = " ")
      sum = n1 + n2
      n1 = n2
      n2 = sum
      
-----------------------------------------------------------------------------------------------------------

## Fibonacci series using while loop

n = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1,end = " ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

-----------------------------------------------------------------------------------------------------------

## Fibonacci series using recursion
def fibonacci_seq(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return(fibonacci_seq(n-1) + fibonacci_seq(n - 2))


n = int(input("Enter number of terms: "))
for i in range(1,n + 1):
    print(fibonacci_seq(i), end = " ")

-----------------------------------------------------------------------------------------------------------
