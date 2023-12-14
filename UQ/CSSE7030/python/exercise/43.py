#统一str小写格式name.lower()
'''
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday'''
a=1
while a==1 :
	a=0
	i=input('please write the first word:')
	i=i.lower()
	if i=='m':
		print('Monday')
	elif i=='t':
		j=input('please write the second word:')
		j=j.lower()
		if j=='u':
			print('Tuesday')
		elif j=='h':
			print('Thursday')
		else:
			print('***')
			a=1
	elif i=='w':
		print('Wednesday')
	elif i=='f':
		print('Friday')
	elif i=='s':
		j=input('please write the second word:')
		j=j.lower()
		if j=='u':
			print('Sunday')
		elif j=='a':
			print('Saturday')
		else:
			print('+++')
			a=1
	else:
		print('SB')
		a=1