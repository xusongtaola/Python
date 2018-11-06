#coding: utf8
#计算1+2+3+...+n的累积和
n = int(input("请输入n的值："))
total = 0
for i in range(1, 1+n):
 print(str(i-1) + "---" + str(total))
 total += i
print(total)

