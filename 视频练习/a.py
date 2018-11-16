class Person:

	def __init__(self, name, weight):
	 
		self.name = name	#等号右侧是形参，左侧是属性。
		self.weight = weight

	def __str__(self):

	 return("我的名字叫 {0} ,体重是 {1:.2f} 公斤".format(self.name,self.weight))

	def run(self):
	 print("{}爱跑步，跑步锻炼身体。".format(self.name))
	 self.weight -= 0.5

	def eat(self):
	 print("{}是吃货，吃完这顿再减肥".format(self.name))
	 self.weight += 1

xiaoming = Person("小明",75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)
