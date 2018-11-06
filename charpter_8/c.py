def harmonic(n):		#计算n阶调和数
    total = 0.0
    for i in range(1, n+1):
      total += 1.0 / i
    return total
for i in range(1,10):			#0的阶乘在本程序中出错
 print(harmonic(i))
