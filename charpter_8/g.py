def my_sum2(a, b, *c):
 total = a + b
 for i in c:
  total += i
 return total
print(my_sum2(1,2))
print(my_sum2(1,2,3,4,5))
print(my_sum2(1,2,3,4,5,7,8))
