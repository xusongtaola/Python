class Dog:

	def run(self):
		print("小狗lalala")

	@staticmethod			#静态方法(不访问实例/类属性)
	def fly():
		print("小鸟lalala")


Dog.fly()		#与类方法调用相似
