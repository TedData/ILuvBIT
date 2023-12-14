import random

def aaa(n):
	a=[]
	while len(a)!=n:
		i=random.randint(1,n)
		if i not in a:
			a.append(i)
	return a
if __name__=='__main__':
	print(aaa(8))

def bbb(val,list=[]):
	list.append(val)
	return list
list1= bbb(10)
list2= bbb(123,['a','b','c'])
list3= bbb('a')
print(list1)
print(list2)
print(list3)