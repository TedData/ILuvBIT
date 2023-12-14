#倒序循环
a=['one','two','three','four','five']
print(a)
print('='*10)
print(a[::-1])
print('='*10)	
for i in range(len(a)-1,-1,-1):
	print(a[i])
print('='*10)
for j in a[::-1]:
	print(j)
