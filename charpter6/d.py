import getpass
username = input("用户名为：")
passwd = getpass.getpass("密码为：")
a = getpass.getuser()
if username == 'xusongtao' and passwd == '123456':
 print('登陆成功')
 print(a)
else: 
 print('登录失败')
