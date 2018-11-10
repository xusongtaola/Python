def my_sum2(a, b, *c, **d):
 total = a + b
 for i in c:
  total += i
 for key in d:
  total += d[key]
 return total
# print(c)b不返回该值
print(my_sum2(1,2))
print(my_sum2(1,2,3,4,5))
print(my_sum2(1,2,3,4,5,7,8))
print(my_sum2(1,2,3,4,5,male = 7,famale = 8))


