import sys
filename = sys.argv[1]				#读取本文件
f = open(filename, 'r+', encoding = 'utf8')	#打开文件
line_no = 0					#统计行号
while True:
  line_no += 1					#行号计数器
  line = f.readline()				#读取行信息
  if line:
    print(line_no, ':', line)			#输出行号及内容
  else:
    break
#b = ' asdafasf'
a = f.writelines([f])
f.close()					#关闭所打开的文件
