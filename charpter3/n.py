#coding: utf8
#输出半径为1-n的圆的周长列表
import math
n = int(input("please enter a positive number:"))
for r in range (1, n+1):
 print("r=" + str(r),end= "")		#end=""表示不换行，表示用空格替换'/n'
 print()				#恢复换行（一般默认换行）
 print("p=" + str(2.0 * math.pi * r))
