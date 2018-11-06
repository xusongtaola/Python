#coding: utf8
#判断一个数是否为素数
while True:
 num = int(input("请输入一个大于1的自然数(输入-1停止)："))
 if (num == -1):
  break
 a=0
 if(num <= 0):
  print('您输入的数不符合规范，请重新输入!')
  continue
 if(num == 1):
  print("该数不为素数")
 elif(num == 2):
  print("该数为素数")
 else:	   
  for i in range(2, num):
   if(num%i == 0):
    print("该数不为素数")
    break
   else:
    a += 1
  if(a == num-2):
   print("该数为素数！")


 
  

