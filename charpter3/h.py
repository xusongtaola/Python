#coding utf8
#死循环 Ctrl + C停止程序运行
import math
while True:
 num = float(input("请输入一个正数:"))
 print(str(num), "的平方根为：", math.sqrt(num))
print("Good bye")

