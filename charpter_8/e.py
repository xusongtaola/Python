import random
b = input("请输入数组元素（逗号隔开）：")
a = b.split(',')
def exchange(a, i,j):
 temp = a[i]
 a[i] = a[j]
 a[j] = temp
def shuffle(a):
 n = len(a)
 for i in range(n):
  r = random.randrange(i, n)
  exchange(a, i, r)
 print(a)
 return a
shuffle(a)
c = a
print("这是：", c)
