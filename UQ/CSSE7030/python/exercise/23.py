#将一个正整数因式分解
n=int(input('number:'))
b=str(n)+'='
a=1
while a<n:
	a+=1
	if n%a==0:
		b=b+str(a)+"*"
		n=n/a
		a=1
b=b[0:-1]
print(b)
