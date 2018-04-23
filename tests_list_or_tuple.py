x = ('tuple', False, 3.2, 2)

if type(x) is list:
     print('x is list')
elif type(x) is set:
     print('x is set')
elif type(x) is tuple:
     print('x is tuple')
else:
     print("Neither a list or a set or a tuple")
           
