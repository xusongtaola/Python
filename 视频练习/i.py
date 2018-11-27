#类方法
#@classmethod
#def lalala(cls):
#	pass

class Tool:

	count = 0

	@classmethod
	def tool_count(cls):

		print("工具数量： {}".format(cls.count))

	def __init__(self, name):

		Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("榔头")

Tool.tool_count()
