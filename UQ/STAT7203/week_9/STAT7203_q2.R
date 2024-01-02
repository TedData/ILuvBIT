# STAT7203 Week 9 Q2
X = rnorm(10000*5, mean=0, sd=1) # or just rnorm(10000*5)
X = matrix(X, nrow=10000, ncol=5) # turn into a matrix
sampleMeans = apply(X,1,mean)
sampleSD = apply(X,1,sd)
Upper = sampleMeans + 1.96*sampleSD/sqrt(5)
Lower = sampleMeans - 1.96*sampleSD/sqrt(5)
1 - (sum(Lower>0) + sum(Upper<0))/10000
