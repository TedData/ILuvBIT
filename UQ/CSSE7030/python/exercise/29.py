#多继承
class A(object):
	def test(self):
		print('A----')
'''
class B(object):
	def test(self):
		print('B----')
'''
class C(A):
	def test(self):
		super().test()
		print('C----')
c=C()
print(C.__mro__)
c.test()