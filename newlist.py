#python function that takes a list and return a new list unique elements
def numbers(num):
     x = []
     for a in num:
          if a not in x:
               x.append(a)
     return x

y = [1,1,2,3,3,3,4,6,7,8,5,8,6]
print sorted(numbers(y))
