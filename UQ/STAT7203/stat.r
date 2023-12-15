
#X^2分布
#参数是值，df=(row-1)*(col-1)，结果是概率

pchisq(3.752392, df=2,lower.tail=FALSE)

#矩阵independent

a = c(12,136,12,120,19,101)
row= 3


X = matrix(a, nrow=row, byrow=TRUE)
E = apply(X,1,sum)%o%apply(X,2,sum)/sum(X)
X_2=sum((X-E)^2/E)
p_value = pchisq(X_2, df=(length(a)/row-1)*(row-1),lower.tail=FALSE)

E
X_2
p_value

#正态分布，条件是概率，结果是值

a = 0.05

qnorm(1-a/2)

#T方分布，a为已知条件(概率)，结果为值

a = 0.05
df= 6

qt(1-a/2,df)

#T方分布，参数是值，结果为概率
#算p-value

T = 7.83888
df= 27  #计算的时候别忘了减1


p = pt(T,df,0)
1-p #没有乘以2，是否需要乘以2，自行考虑
2*(1-p)

#计算S^2
S1 = 4.5
N1 = 12

S2 = 5.7
N2 = 12

S_2=(S1^2*(N1-1)+S2^2*(N2-1))/(N1+N2-2)
SE = sqrt(S_2/N1+S_2/N2)


S_2
SE

a = 11.397
b = -0.4884
c = 0.0326
m = 1
n = 25
a*m*m + 2*b*m*n + c*n*n


