x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[15,8,1],[6,7,3],[4,5,9]]
z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
	for j in range(len(x[i])):
		z[i][j]=x[i][j]+y[i][j]
	print(z[i])