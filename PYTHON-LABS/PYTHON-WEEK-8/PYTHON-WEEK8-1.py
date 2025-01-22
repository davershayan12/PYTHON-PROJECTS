def max_list(list):
   max = list[0]
   for a in list:
       if a > max:
            max = a
   return max 
print(max_list([1,2,-8,0]))
