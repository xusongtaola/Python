class Female:
	def __init__(self, name):
		self.name = name
		self.age = 18
	def __secret(self):
		print("{0}的年龄是{1}".format(self.name, self.age))

xiaofang = Female("小芳")

print(xiaofang.age)

xiaofang.__secret()
xiaofang._Female__secret()

