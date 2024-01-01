X = matrix(c(24,11,9,34,9,4),nrow=2,byrow=TRUE)
chisq.test(X)

E = apply(X,1,sum)%o%apply(X,2,sum)/sum(X)
E
X2 = sum((X-E)^2/E)
X2
pval = pchisq(X2, df=2, lower.tail=FALSE)
pval
