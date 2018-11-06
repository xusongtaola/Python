import sys
n = int(sys.argv[1])
sum = 0
for i in range(n):
 num = int(input('请输入一整数：'))
 sum += num
print('累积和为：', sum)
