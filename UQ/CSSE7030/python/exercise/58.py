#取十个数排序
import random
def num():
	i=[]
	while len(i)<10:
		r=random.randint(1,10)
		for j in i:
			if r==j:
				break
		else:
			i.append(r) 
	i.sort()
	return i

print(num())
