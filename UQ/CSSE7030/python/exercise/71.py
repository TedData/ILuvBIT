def compare(x, y):
	natation = ['>', '<', '=']
	if x > y :
		print(x,natation[0],y,sep='')
	elif x < y :
		print(x,natation[1],y,sep='')
	else :
		print(x,natation[2],y,sep='')
compare(20, 10) 
compare(1, 50)
compare(6, 6)