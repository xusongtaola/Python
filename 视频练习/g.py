#多态
class Dog:

	def __init__(self, name):

		self.name = name
	
	def game(self):
	
		print("{}在玩".format(self.name))

class lala(Dog):

	def game(self):

		print("{}在天上玩".format(self.name))

class Person:

	def __init__(self, name):

		self.name = name

	def game_player(self, dog):

		print("{0} 和 他的狗 {1}在玩".format(self.name, dog.name))
		
		#让狗玩
		dog.game()

wangcai = lala("旺财")

xiaoming = Person("小名")

xiaoming.game_player(wangcai)
