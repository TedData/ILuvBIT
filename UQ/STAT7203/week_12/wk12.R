setwd("C:/Users/Harrison/Desktop/STAT7203/wk12")
hubble = read.csv("hubble.csv", header=TRUE)
head(hubble)
hubblelm = lm(velocity~distance, data=hubble)
# lm(formula= Y ~ X, data=dataset)
summary(hubblelm)
plot(hubblelm)


# b) test H0: B0 = 0, vs. H1: B0 != 0
# from summary(), t=0.053, pval=0.958
# no evidence to reject H0

# c) 99% CI for B1
# do by hand first
# estimate +- (critical value) * S.E.(estimate)
est = 76.127; seest = 9.493
df = 24-2  # number of observations - number things
            # we are estimating (intercept and slope)
alpha = 0.01 #1-0.99 = alpha
conflevel = 0.995
critval = qt(conflevel, df)
est; seest; critval
ub = est + critval*seest
lb = est - critval*seest
lb; ub
# using built in functions
confint(hubblelm, level=0.99)

#d) 95% CI for etc.
# est mean velocity of two galaxies separated by
# 10 Mega pasecs is 
est = 6.696+76.127*10
est
sumhubble = summary(hubblelm)
sumhubble
XTXinv = sumhubble$cov.unscaled
xnew = c(1,10)
t(xnew) %*% XTXinv %*% xnew

seest = sumhubble$sigma * sqrt(t(xnew) %*% XTXinv %*% xnew)
critval = qt(0.975, 22)
ub = est + critval*seest
lb = est - critval*seest
lb; ub
