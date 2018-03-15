def factorial(n):
     if n == 0:
          return 1
     else:
          return n * factorial(n-1)
num = int(input("number to compare the factorial"))

print(factorial(num))


