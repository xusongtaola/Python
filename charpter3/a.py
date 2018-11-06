#coding: utf8
Forbid = ["考前答案", "枪手网", "窃听器", "替考"]
into = input('请输入评论： ')  
for i in Forbid:
    if i in into:
        l = len(i)
        into=into.replace(i,'*'*l)
print(into)
