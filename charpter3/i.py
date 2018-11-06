#coding utf8
#for-else语句练习：输入爱好
hobbies = ""
for i in range(1, 3 + 1):
 s = input("请输入爱好之一（最多3个，按Q或q结束）：")
 if s.upper() == 'Q':
  break
 hobbies += s + '   '
else:
 print('您输入了三个爱好。')
if(len(s) == 1):
 print("您难道没有爱好吗？要不要想一想呢？")
else:
 print('您的爱好为：', hobbies)
