#coding: utf8
class HouseItem:

	def __init__(self, name, area):

		self.name = name
		self.area = area

	def __str__(self):

		return("{0}占地{1:.2f} ".format(self.name, self.area))

class House:

	def __init__(self, house_type, area):

		self.house_type = house_type
		self.area = area

		#剩余面积
		self.free_area = area

		#家具名称列表
		self.item_list = []

	def __str__(self):

		return("户型： {0}\n总面积： {1}【剩余: {2:.2f}】\n家具： {3}".format(self.house_type, self.area, self.free_area, self.item_list))

	def add_item(self, item):

		print("要加入 {}".format(item))

		if self.free_area < item.area:

			print("{}的面积太大了，无法添加".format(item.name))
		else:

			self.item_list.append(item.name)

			self.free_area -= item.area
#1.创建家具
bed = HouseItem("席梦思",40)
print(bed)
chest = HouseItem("衣柜",2)
print(chest)
table = HouseItem("餐桌",1.5)
print(table)

#2.创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
