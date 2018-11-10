def my_sum1(mid_score, end_score, mid_rate = 0.4): #期中/期末成绩/期中成绩比重
 #基于以上计算总评成绩
 score = mid_score * mid_rate + end_score * (1 - mid_rate)
 print(format(score, '.2f'))
 print("该学生成绩为：{:#>16}".format(score))
my_sum1(88, 79)
my_sum1(88, 79, 0.5)
my_sum1(mid_score = 88, end_score = 79)
my_sum1(end_score = 79, mid_score = 88)
