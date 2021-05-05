'''Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
  The desired output is like :

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]'''


x, y = 1, 1
list_fib = []
while x <= 55:
    list_fib.append(x)
    x, y = y, x + y
print(list_fib)
