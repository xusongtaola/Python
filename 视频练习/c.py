class Gun:

	def __init__(self, model):
		self.model = model
		self.bullet_count = 0

	def add_bullet(self, count):

		self.bullet_count += count

	def shoot(self):
		if self.bullet_count > 0:
			self.bullet_count -= 1
			print("[{0}嗒嗒嗒嗒【子弹数{1}】".format(self.model, self.bullet_count))
		else:
			print("{0}没有子弹了".format(self.model))

class Soldier:
	
	def __init__(self, name):

		self.name = name
		self.gun = None

	def fire(self):
		if self.gun == None:
			print("{}还没有枪".format(self.name))
		else:
			print("冲阿，{}".format(self.name))
			self.gun.add_bullet(50)
			self.gun.shoot()

xusanduo = Soldier("xusanduo")

#ak47 = Gun("AK47")	

#xusanduo.gun = ak47

xusanduo.fire()

