#coding: utf8
#输出前n个2的乘幂的值列表
n = int(input("请输入n的值："))
power = 1
for i in range(n):
 print(str(i) + "---" + str(power))
 power *= 2
