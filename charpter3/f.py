#coding: utf8
num = 0; scores = 0; 		#初始化学生成绩
while True :
 s = input("请输入学生成绩（按q或Q结束）：")
 if s.upper() == 'Q':
  break
 if float(s) < 0: 		#输入的成绩必须大于0
  continue
 num += 1    			#统计学生人数
 scores += float(s) #计算学生成绩总和
print("学生人数为：{0},平均成绩为:{1}".format(num,scores / num))
