
dev.new(width=5, height=4) # set the figure size to be 5in x 4in

library("readr")
fheight<-read_csv("./PearsonFather.csv",col_names="fheight",col_types="d")
sheight<-read_csv("./PearsonSon.csv",col_names="sheight",col_types="d")
fs_height<-data.frame(fheight,sheight)
plot(fs_height$fheight,fs_height$sheight,main="Father and Son Heights", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
summary(fs_height)

lmfit<-with(fs_height,lm(sheight~fheight))
summary(lmfit)

lmfit.res<-resid(lmfit)
plot(fs_height$fheight,lmfit.res,
     main="Residual Son Heights from Simple Linear Regression", 
     xlab="Father Heights (in)",
     ylab="Residual Son Heights (in)",
     col=rgb(1,0.3,0.1,0.5))
summary(lmfit.res)

library("car")
qqPlot(lmfit.res,xlab="Standard Normal Quantiles",ylab="Quantiles of the Residuals")

shapiro.test(lmfit.res)

summary(lmfit)

confint(lmfit)

predict(lmfit, data.frame(fheight=67))

predict(lmfit,data.frame(fheight=67),interval="confidence",level = 0.95,type="response")

newfheight<-seq(min(fheight$fheight)-1, max(fheight$fheight)+1, by=0.1)
lmfitci<-predict(lmfit,data.frame(fheight=newfheight),interval="confidence",level = 0.95,type="response")
plot(fs_height$fheight,fs_height$sheight,main="Father and Son Heights", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
lines(newfheight,lmfitci[,1],col="black",lty=1)
lines(newfheight,lmfitci[,2],col="black",lty=2)
lines(newfheight,lmfitci[,3],col="black",lty=2)

predict(lmfit,data.frame(fheight=67),interval="predict",level=0.95,type="response")

newfheight<-seq(58,76)
lmfitpi<-predict(lmfit,data.frame(fheight=newfheight),interval="prediction",level = 0.95,type="response")
plot(fs_height$fheight,fs_height$sheight,main="Father and Son Heights", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
lines(newfheight,lmfitpi[,1],col="black",lty=1)
lines(newfheight,lmfitpi[,2],col="black",lty=2)
lines(newfheight,lmfitpi[,3],col="black",lty=2)

lmfitpi<-predict(lmfit,data.frame(fheight=fheight$fheight),interval="prediction",level = 0.95,type="response")
mean((sheight$sheight > lmfitpi[,2]) & (sheight$sheight < lmfitpi[,3]))

set.seed(107)
N = length(fheight$fheight)
trainidx = sample(1:N, floor(0.7*N), replace=FALSE)
tr = data.frame(fheight=fheight$fheight[trainidx], sheight=sheight$sheight[trainidx])
ts = data.frame(fheight=fheight$fheight[-trainidx], sheight=sheight$sheight[-trainidx])

lmfit = lm(sheight ~ fheight, data=tr)
cat('MSE on training set:', mean((predict(lmfit, tr) - tr$sheight)**2), '\n')
cat('MSE on test set:', mean((predict(lmfit, ts) - ts$sheight)**2), '\n')

library("readr")
HR_comma_sep <- read_csv("https://stluc.manta.uqcloud.net/mdatascience/public/datasets/HumanResourceAnalytics/HR_comma_sep.csv")
HR_best <- HR_comma_sep[(HR_comma_sep$last_evaluation>=0.8)&(HR_comma_sep$time_spend_company>=4),]
head(HR_best,10)
summary(HR_best)
set.seed(8888) # Set a seed for the random number generator;
trainidx<-sample(nrow(HR_best), floor(nrow(HR_best) * 0.5))
HR_best_train<-HR_best[trainidx,]
HR_best_test<-HR_best[-trainidx,]

plot(HR_best_train$average_montly_hours,HR_best_train$left,main="Left vs Average Monthly Hours Worked (Best)", xlab="Average Monthly Hours",ylab="Left",col=rgb(0,0,1,0.5))

logfit<-glm(left~average_montly_hours,data=HR_best_train,family=binomial)
summary(logfit)
newamh<-seq(96,310)
predprobs<-predict(logfit,data.frame(average_montly_hours=newamh),type="response")
plot(HR_best_train$average_montly_hours,HR_best_train$left,main="Left vs Average Monthly Hours Worked (Best)", xlab="Average Monthly Hours",ylab="Left",col=rgb(0,0,1,0.5))
lines(newamh,predprobs,col="black",lty=1)

HR_best_train$probs<-predict(logfit,data.frame(average_montly_hours=HR_best_train$average_montly_hours),type="response")
HR_best_train$predleft<-as.integer(HR_best_train$probs>=0.5)
table(HR_best_train$predleft,HR_best_train$left)

HR_best_test$probs<-predict(logfit,data.frame(average_montly_hours=HR_best_test$average_montly_hours),type="response")
HR_best_test$predleft<-as.integer(HR_best_test$probs>=0.5)
table(HR_best_test$predleft,HR_best_test$left)

set.seed(1)
N = dim(HR_best_train)[1]

idx = sample(1:N, floor(0.5*N), replace=FALSE)
HR_best_train1 = HR_best_train[idx,]
HR_best_train2 = HR_best_train[-idx,]

logfit_f1 <- glm(left~average_montly_hours, data=HR_best_train1,family=binomial)
logfit_f2 <- glm(left~average_montly_hours, data=HR_best_train2,family=binomial)

pred1 <-as.integer(predict(logfit_f2, HR_best_train1, type="response") >= 0.5)
pred2 <-as.integer(predict(logfit_f1, HR_best_train2, type="response") >= 0.5)

cat('2-fold CV error is ', 0.5*(mean(pred1 != HR_best_train1$left) + mean(pred2 != HR_best_train2$left)),'\n')

library("ROCR")
trainROC<-performance(prediction(HR_best_train$probs,HR_best_train$left),"tpr","fpr")
plot(trainROC)
abline(a=0, b= 1,lty=2)
trainAUC<-as.double(performance(prediction(HR_best_train$probs,HR_best_train$left),"auc")@y.values)
trainAUC

testROC <- performance(prediction(HR_best_test$probs,HR_best_test$left),'tpr','fpr')
plot(testROC)
abline(a=0, b=1, lty=2)
testAUC <- as.double(performance(prediction(HR_best_test$probs,HR_best_test$left), 'auc')@y.values)
testAUC

logfit2<-glm(left~average_montly_hours*satisfaction_level*number_project,data=HR_best_train,family=binomial)
summary(logfit2)

HR_best_train$probs2<-predict(logfit2,data.frame(average_montly_hours=HR_best_train$average_montly_hours,satisfaction_level=HR_best_train$satisfaction_level,number_project=HR_best_train$number_project),type="response")
trainROC2<-performance(prediction(HR_best_train$probs2,HR_best_train$left),"tpr","fpr")
plot(trainROC2)
abline(a=0, b= 1,lty=2)
trainAUC2<-as.double(performance(prediction(HR_best_train$probs2,HR_best_train$left),"auc")@y.values)
trainAUC2

HR_best_test$probs2 <- predict(logfit2,data.frame(average_montly_hours=HR_best_test$average_montly_hours,satisfaction_level=HR_best_test$satisfaction_level,number_project=HR_best_test$number_project),type="response")
testROC2 <- performance(prediction(HR_best_test$probs2, HR_best_test$left), 'tpr', 'fpr')
plot(testROC2)
abline(a=0, b=1, lty=2)
testAUC2 <- as.double(performance(prediction(HR_best_test$probs2, HR_best_test$left), 'auc')@y.values)
testAUC2

logfit_f1 <- glm(left~average_montly_hours*satisfaction_level*number_project, data=HR_best_train1,family=binomial)
logfit_f2 <- glm(left~average_montly_hours*satisfaction_level*number_project, data=HR_best_train2,family=binomial)

pred1 <-as.integer(predict(logfit_f2, HR_best_train1, type="response") >= 0.5)
pred2 <-as.integer(predict(logfit_f1, HR_best_train2, type="response") >= 0.5)
pred <-as.integer(predict(logfit2, HR_best_test, type="response") >= 0.5)

cat('2-fold CV error is ', 0.5*(mean(pred1 != HR_best_train1$left) + mean(pred2 != HR_best_train2$left)),'\n')
cat('test set error is ', mean(pred != HR_best_test$left))

library("MASS")
ldafit<-lda(left~average_montly_hours*satisfaction_level*number_project,data=HR_best_train)
temp<-predict(ldafit,data.frame(average_montly_hours=HR_best_test$average_montly_hours,satisfaction_level=HR_best_test$satisfaction_level,number_project=HR_best_test$number_project),type="response")
HR_best_test$probs3<-temp$posterior[,2]
testROC3<-performance(prediction(HR_best_test$probs3,HR_best_test$left),"tpr","fpr")
plot(testROC3)
abline(a=0, b= 1,lty=2)
testAUC3<-as.double(performance(prediction(HR_best_test$probs3,HR_best_test$left),"auc")@y.values)
testAUC3

library("MASS") 
qdafit<-qda(left~average_montly_hours*satisfaction_level*number_project,data=HR_best_train) 
temp<-predict(qdafit,data.frame(average_montly_hours=HR_best_test$average_montly_hours,satisfaction_level=HR_best_test$satisfaction_level,number_project=HR_best_test$number_project), type="response") 
HR_best_test$probs4<-temp$posterior[,2] 
testROC4<-performance(prediction(HR_best_test$probs4,HR_best_test$left),"tpr","fpr") 
plot(testROC4) 
abline(a=0, b= 1,lty=2) 
testAUC4<-as.double(performance(prediction(HR_best_test$probs4,HR_best_test$left),"auc")@y.values) 
testAUC4

HR_left<-HR_comma_sep[HR_comma_sep$left==1,]
head(HR_left)

library("ggplot2") # Expanded plotting functionality over "lattice" package
x<-cbind(HR_left$average_montly_hours,HR_left$satisfaction_level,HR_left$last_evaluation)
kmfit<-kmeans(x,3,nstart=25) # Find the best 3 clusters using 25 random sets of (distinct) rows in x as initial centres.
pairs(x,col=(kmfit$cluster),labels=c("Av. Mon. Hrs","Sat. Lvl","Last Eval."))

x<-cbind(HR_left$average_montly_hours,100*HR_left$satisfaction_level,100*HR_left$last_evaluation)
kmfit<-kmeans(x,3,nstart=25) # Find the best 3 clusters using 25 random restarts
pairs(x,col=(kmfit$cluster),labels=c("Av. Mon. Hrs","Sat. Lvl","Last Eval."))

# Get the three clusters; these are three clusters for employees that have left
c1 <- subset(HR_left, kmfit$cluster == 1)
c2 <- subset(HR_left, kmfit$cluster == 2)
c3 <- subset(HR_left, kmfit$cluster == 3)

# Determine which cluster is which from the above pairs plot
par(mfrow=c(1,3))

plot(c1$last_evaluation*100,c1$average_montly_hours, xlim=c(0,100), ylim=c(100, 300))
plot(c2$last_evaluation*100,c2$average_montly_hours, xlim=c(0,100), ylim=c(100, 300))
plot(c3$last_evaluation*100,c3$average_montly_hours, xlim=c(0,100), ylim=c(100, 300))

# Cluster formatting to reference
color.c1 <- rgb(0, 0, 0, 0.8) # black
color.c2 <- rgb(1,0,0,0.8) # red
color.c3 <- rgb(36/255, 199/255, 24/255, 0.8) # green

# Summary of each cluster
summary(c1)
summary(c2)
summary(c3)

# Create multiple figure
par(mfrow=c(2,1))

# Histogram - frequency
hist(c1$average_montly_hours, col=color.c1,freq=T, main='Histogram for Average Monthly Hours by Clusters',
    xlab='Average Monthly Hours', ylim=c(0,500))
hist(c2$average_montly_hours, col=color.c2,freq=T, add=TRUE)
hist(c3$average_montly_hours, col=color.c3, freq=T, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)

# Histogram - density
hist(c1$average_montly_hours, col=color.c1,freq=FALSE, main='Density plot for Average Monthly worked by Clusters',
    xlab='Average Monthly Hours', ylim=c(0,0.05))
hist(c2$average_montly_hours, col=color.c2,freq=FALSE, add=TRUE)
hist(c3$average_montly_hours, col=color.c3, freq=FALSE, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)

# Create multiple figure
par(mfrow=c(2,1))

# Histogram - frequency
hist(c1$time_spend_company, col=color.c1,freq=T, main='Histogram for Time Spent at Company by Clusters',
    xlab='Time Spent at Company', ylim=c(0,1500))
hist(c2$time_spend_company, col=color.c2,freq=T, add=TRUE)
hist(c3$time_spend_company, col=color.c3, freq=T, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)

# Histogram - density
hist(c1$time_spend_company, col=color.c1,freq=FALSE, main='Density plot for Time Spent at Company by Clusters',
    xlab='Time Spent at Company', ylim=c(0,2.5))
hist(c2$time_spend_company, col=color.c2,freq=FALSE, add=TRUE)
hist(c3$time_spend_company, col=color.c3, freq=FALSE, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)

cluster_table_sales <- table(HR_left$sales, kmfit$cluster)
mosaicplot(cluster_table_sales, las=2, main='Mosaic Plot of Clusters by Department', xlab='Department', ylab='Cluster')

cluster_table_salary <- table(HR_left$salary, kmfit$cluster)
mosaicplot(cluster_table_salary, las=2, main='Mosaic Plot of Clusters by Salary', xlab='Salary', ylab='Cluster')

# Create multiple figure
par(mfrow=c(2,1))

# Histogram - frequency
hist(c1$number_project, col=color.c1,freq=T, main='Histogram for Number of Projects by Clusters',
    xlab='Number of Projects', ylim=c(0,1500))
hist(c2$number_project, col=color.c2,freq=T, add=TRUE)
hist(c3$number_project, col=color.c3, freq=T, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)

# Histogram - density
hist(c1$number_project, col=color.c1,freq=FALSE, main='Density plot for Number of Projects by Clusters',
    xlab='Number of Projects', ylim=c(0,2.5))
hist(c2$number_project, col=color.c2,freq=FALSE, add=TRUE)
hist(c3$number_project, col=color.c3, freq=FALSE, add=TRUE)
legend('topleft', c('1', '2', '3'), fill=c(color.c1, color.c2, color.c3), cex=0.5)
