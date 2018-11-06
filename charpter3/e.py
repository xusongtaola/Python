#coding: utf8
import math
while True :
 m = int(input("请输入一个整数（>1）(且输入0结束)："))
 if(m == 0): break
 if(m <= 1):
  print("您输入的数不符合规范，请重新输入！")
  continue
 k = int(math.sqrt(m))
 for i in range(2, k+2):
  if m % i == 0:
   break    					#因为有整除数，所以不是。
 if  i == k+1 :
  print(m, "是素数！")
 else:
  print(m, "是合数")
