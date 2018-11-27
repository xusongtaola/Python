#记录创建工具对象的数目
class Tool:

	count = 0

	def __init__(self, name):
		self.name = name

		Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("刀子")

print(Tool.count)
