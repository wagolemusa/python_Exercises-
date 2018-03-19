def max_num_list(num):
     max = num[0]
     for a in num:
          if a > max:
               max = a
     return max
print(max_num_list([2,4,6,8,5]))
