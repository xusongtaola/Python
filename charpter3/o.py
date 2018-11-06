#coding utf8
#牛顿迭代法计算平方根
EPSILON = 1e-15
a = float(input("请输入正实数a： "))
t = a
while abs(t - a/t) > (EPSILON * t):
 print(t)
 t = (a/t +t) / 2.0
print(t)

