j = 0   			#控制一行显示的数值个数
print('100~200之间不能被3整除的数为：')
for i in range(100, 200 + 1):
 if (i % 3 == 0):continue
 print(str.format("{0:<5}",i), end="")   #每个数占5个位置，不足后面加空格，并且
					 #不换行
 j += 1
 if j % 10 == 0 : print()   		#一行显示10个数后换行
