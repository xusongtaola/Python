class Game:

	#类属性（直接赋值）
	top_score = 0
	
	#实例属性（初始化方法中）
	def __init__(self, name):
		self.player_name = name

	#静态方法
	@staticmethod
	def show_help():
		print("帮助信息：阻止僵尸")
	
	#类方法
	@classmethod
	def show_top_score(cls):
		print("历史记录： {}".format(cls.top_score))

	#实例方法
	def start_game(self):
		print("{}开始游戏啦...".format(self.player_name))
		
		#实例方法调用类属性
		print("{}:just a test".format(Game.top_score))
#主程序

#1.查看游戏帮助信息

Game.show_help()

#2.查看历史最高分

Game.show_top_score()

#3.创建游戏对象

game = Game("小名")

game.start_game()
