#Python3 中默认基类为object（新式类）

class A(object):
 	pass
a = A()

print(dir(a))

class B:
	pass

b = B()

print(dir(b))
