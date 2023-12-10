
library(readr)
data <- read_csv("./student_data_anon.csv")
data <- data[complete.cases(data),]
summary(data)
mean(data$age)

datasample<-data[sample(1:nrow(data),100,replace=TRUE),]
mean(datasample$GPA)

aggregate(GPA~gender, datasample, mean)
aggregate(GPA~gender, datasample, length)

meanGPAbygender<-data.frame(sample=integer(),FGPA=double(),MGPA=double())
for (i in 1:1000){
    datasample<-data[sample(1:nrow(data),100,replace=TRUE),]
    temp<-as.data.frame(aggregate(GPA~gender, datasample, mean))
    temp$gender<-NULL
    meanGPAbygender[i,]<-c(i,t(temp))
}

summary(meanGPAbygender)

hist(meanGPAbygender$MGPA, col=rgb(0,0,1,0.5),main="Bootstrapped Histogram for Mean GPA by Gender", xlab="Mean GPA")
hist(meanGPAbygender$FGPA, col=rgb(1,0,0,0.5),add=TRUE)
legend("topright", c("Male","Female"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

# Generate some random weights which are non-negative and sum to 1
data$weights<-runif(nrow(data))
data$weights<-data$weights/sum(data$weights)

weighteddatasample<-data[sample(1:nrow(data),100,replace=TRUE,data$weights),]

meanGPAbygenderWeighted<-data.frame(sample=integer(),MGPA=double(),FGPA=double())
for (i in 1:1000){
  datasample<-data[sample(1:835,100,replace=TRUE,data$weights),]
  temp<-as.data.frame(aggregate(GPA~gender, datasample, mean))
  temp$gender<-NULL
  meanGPAbygenderWeighted[i,]<-c(i,t(temp))
}

hist(meanGPAbygenderWeighted$MGPA, col=rgb(0,0,1,0.5),main="Bootstrapped Histogram for Mean GPA by Gender, Weighted", xlab="Mean GPA")
hist(meanGPAbygenderWeighted$FGPA, col=rgb(1,0,0,0.5),add=TRUE)
legend("topright", c("Male","Female"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

sv<-data.frame(variable=double(),strata=integer())
sv[1:10,1]<-rnorm(10)
sv[1:10,2]<-as.numeric(sv[,1]>0)

sv0<-sv[sv$strata==0,]$variable
sv1<-sv[sv$strata==1,]$variable

sv0sample<-sv0[sample(1:length(sv0),3,replace=TRUE)]
sv1sample<-sv1[sample(1:length(sv1),3,replace=TRUE)]
svsample<-rbind(sv0sample,sv1sample)

sv0sample<-sv[sample(1:nrow(sv), 3, replace=TRUE,prob=(sv$strata==0)), 'variable']
sv1sample<-sv[sample(1:nrow(sv), 3, replace=TRUE,prob=(sv$strata==1)), 'variable']
svsample<-rbind(sv0sample,sv1sample)

mgpa = c()
fgpa = c()
for (i in 1:1000){
    mgpa = c(mgpa, mean(data[sample(1:nrow(data), 50, replace=TRUE,prob=data$gender=="M"), "GPA", drop=TRUE]) )
    fgpa = c(fgpa, mean(data[sample(1:nrow(data), 50, replace=TRUE,prob=data$gender=="F"), "GPA", drop=TRUE]) )
}
hist(mgpa, col=rgb(0,1,0,.2))
hist(fgpa, add=TRUE, col=rgb(1,0,0,.2))

for (s in 1:5) {
    print(mean(data[seq(s, 835, 5),]$GPA))
}
