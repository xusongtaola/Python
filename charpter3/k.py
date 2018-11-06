#coding: utf8
#输出小于或等于n的最大的2的乘幂的值
n = int(input("please enter a positive number:"))
power = 1
while 2*power <= n :		#判断比较n与乘幂的大小
 power *= 2
print(power)
