#coding: utf8
#计算并输出n的阶乘
n = int(input("please enter a positive number:"))
factorial = 1
for i in range(1, n+1):
 print(str(i-1) + "---" + str(factorial))
 factorial *= i
print(factorial)
