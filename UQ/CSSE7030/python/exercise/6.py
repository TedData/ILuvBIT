#随机分配name到rooms里
import random
name=['a','b','c','d','e','f','g','h']
rooms=[[],[],[]]
for temp in name:
	i=random.randint(0,2)
	rooms[i].append(temp)	
print(rooms)
j=1
for room in rooms:
	print(room)
	print('people is '+str(len(rooms[j-1])))
	print('room %d is '%j,end=(''))
	for name1 in room:

		print(name1,end=(' '))
	print('')
	j+=1




'''
a=[]
b=[]
c=[]
for temp in name:
	i=random.randint(1,3)
	if i==1:
		a.append(temp)
	elif i==2:
		b.append(temp)
	else:
		c.append(temp)
print(a)
print(b)
print(c)
'''