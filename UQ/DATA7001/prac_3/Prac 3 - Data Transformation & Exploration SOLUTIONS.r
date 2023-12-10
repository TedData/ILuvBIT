
char_var <- "12345" 
num_var <- 12345 
class(char_var)
class(num_var)

a <- c(15, 20, 1, 10)
b <- c("15", "1", "4")

# Valid! We can compute the mean of numberic values.
print(mean(a))
# You can't compute the mean from a set of characters by a number.
print(mean(b))

b <- c("15", "1", "4")
mean(as.numeric(b))

library(readr)
oswego <- read_csv("OswegoTutorial.csv")

head(oswego)

dim(oswego)

oswego$age

mean(oswego$age)

class(oswego$age)

oswego$age[oswego$age == "seven"] <- "7"

### Solution 1
OmitNA<-na.omit(oswego$age) # The NA value is omitted and remaining data is stored in OmitNA
AsNum<-as.numeric(OmitNA) # OmitNA from previous step is stored as numberic in AsNum
mean(AsNum) # Mean is calculated

### Solution 2 (break this one-liner down to understand it)
mean(as.numeric(oswego$age)[!is.na(oswego$age)])

### Solution 3 (a neater solution)
mean(as.numeric(oswego$age), na.rm=TRUE)

library(tidyr)

oswego_new <- separate(oswego, onsetdate, into = c("onset_day", "onset_month"), sep = "-")
head(oswego_new)

oswego[24,'onsetdate'] = '18-Apr'
oswego_new <- separate(oswego, onsetdate, into = c("onset_day", "onset_month"), sep = "-")

unique(oswego_new$onset_month)

library(tidyr)
oswego_address_separate <- separate(oswego, address, into = c("address", "suburb_name", "state", "postcode"), sep = ",")
head(oswego_address_separate)

###### Solution 1
#filter data with those who are ill
oswego_ill <- oswego_address_separate[oswego_address_separate[,4]=="yes",]

#aggregate by postcode
Postcode_Count = aggregate(ill~postcode, oswego_ill, length)

#find and display postcode with maximum occurances of ill
Postcode_Max <- Postcode_Count[Postcode_Count[,2]== max(Postcode_Count$ill), ] 
Postcode_Max

##### Solution 2
#filter data with those who are ill
oswego_ill <- oswego_address_separate[oswego_address_separate[,4]=="yes",]

#generate a frequency table
freqs = table(oswego_ill[,'postcode'])

#find and display postcode with maximum occurrances of ill
freqs[freqs==max(freqs)]
#also try which(freqs==max(freqs)), and names(which(freqs==max(freqs)))

Postcode_Count

oswego_address_separate$age = as.numeric(oswego_address_separate$age)
df = aggregate(cbind(age=age, count=1) ~ postcode, oswego_address_separate, sum)
df$age = df$age / df$count
df

oswego_address_separate$age[oswego_address_separate$postcode == ' 4021']

library(readr)
HR_comma_sep <- read_csv("https://stluc.manta.uqcloud.net/mdatascience/public/datasets/HumanResourceAnalytics/HR_comma_sep.csv")
HR_comma_sep

sum(!complete.cases(HR_comma_sep))

summary(HR_comma_sep)

test_table<-table(HR_comma_sep$sales,HR_comma_sep$left)
test_table

margin.table(test_table) 
margin.table(test_table,1)
margin.table(test_table,2)

prop.table(test_table)
prop.table(test_table,1)
prop.table(test_table,2)

mosaicplot(test_table,main="Mosaic Plot of Left by Department",xlab="Department",ylab="Left",las=2)

boxplot(HR_comma_sep$average_montly_hours~HR_comma_sep$left,xlab="Left",ylab="Average Monthly Hours",main="Boxplot of Average Monthly Hours by Left")

hist(HR_comma_sep$average_montly_hours[HR_comma_sep$left==1], col=rgb(1,0,0,0.5),main="Histogram for Average Monthly Hours by Left", xlab="Average Monthly Hours")
hist(HR_comma_sep$average_montly_hours[HR_comma_sep$left==0], col=rgb(0,0,1,0.5),add=TRUE)
legend("topright", c("Not Left","Left"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

E0<-ecdf(HR_comma_sep$average_montly_hours[HR_comma_sep$left==0])
E1<-ecdf(HR_comma_sep$average_montly_hours[HR_comma_sep$left==1])
plot(E0,col=rgb(0,0,1,0.5),verticals = TRUE, do.points = FALSE,main="ECDF for Average Monthly Hours by Left", xlab="Average Monthly Hours")
plot(E1,col=rgb(1,0,0,0.5),verticals = TRUE, do.points = FALSE,add=TRUE)
legend("bottomright", c("Not Left","Left"),lwd=1, lty=c(1,1),col=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

par(mfrow=c(2,1)) # Create 2 by 1 figure
# Plot Frequencies
hist(HR_comma_sep$time_spend_company[HR_comma_sep$left==0],breaks=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5),col=rgb(0,0,1,0.5),main="Histogram for Time Spent at Company by Left", xlab="Time Spent at Company (Years)",freq=TRUE)
hist(HR_comma_sep$time_spend_company[HR_comma_sep$left==1],breaks=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5),col=rgb(1,0,0,0.5),add=TRUE,freq=TRUE)
legend("topright", c("Not Left","Left"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

# Plot Proportions
hist(HR_comma_sep$time_spend_company[HR_comma_sep$left==1],breaks=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5),col=rgb(1,0,0,0.5),main="Density for Time Spent at Company by Left", xlab="Time Spent at Company (Years)",freq=FALSE)
hist(HR_comma_sep$time_spend_company[HR_comma_sep$left==0],breaks=c(0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5),col=rgb(0,0,1,0.5),add=TRUE,freq=FALSE)
legend("topright", c("Not Left","Left"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

# Plot Density
hist(HR_comma_sep$last_evaluation[HR_comma_sep$left==1],col=rgb(1,0,0,0.5),main="Histogram for Last Evaluation at Company by Left", xlab="Last Evaluation",freq=FALSE)
hist(HR_comma_sep$last_evaluation[HR_comma_sep$left==0],col=rgb(0,0,1,0.5),add=TRUE,freq=FALSE)
legend("topright", c("Not Left","Left"),fill=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

HR_management = subset(HR_comma_sep, sales == 'management' & left == 1)
HR_hr = subset(HR_comma_sep, sales == 'hr' & left==1)

hist(HR_hr$average_montly_hours, col=rgb(1,0,0,0.5), freq=FALSE,
     main="Density for Average Monthly Hours by Left", xlab="Average Monthly Hours")
hist(HR_management$average_montly_hours, col=rgb(0,0,1,0.5), freq=FALSE, add=TRUE)
legend("topright", c("HR", "Management"),pch=c(1,1),col=c(rgb(1,0,0,0.5), rgb(0,0,1,0.5)))

hist(HR_hr$satisfaction_level, col=rgb(1,0,0,0.5), freq=FALSE,
    main="Density for Satisfaction Level by Left", xlab="Satisfaction")
hist(HR_management$satisfaction_level, col=rgb(0,0,1,0.5), freq=FALSE, add=TRUE)
legend("topright", c("HR", "Management"),pch=c(1,1),col=c(rgb(1,0,0,0.5), rgb(0,0,1,0.5)))

hist(HR_hr$number_project, col=rgb(1,0,0,0.5), freq=FALSE, 
     main="Density for Average Monthly Hours by Left", xlab="Average Monthly Hours")
hist(HR_management$number_project, col=rgb(0,0,1,0.5), freq=FALSE, add=TRUE)
legend("topright", c("HR", "Management"),pch=c(1,1),col=c(rgb(1,0,0,0.5), rgb(0,0,1,0.5)))

plot(HR_comma_sep$average_montly_hours[HR_comma_sep$left==0],HR_comma_sep$last_evaluation[HR_comma_sep$left==0],main="Scatter Plot for Average Monthly Hours vs \n Last Evalation by Left", xlab="Average Monthly Hours",ylab="Last Evaluation",col=rgb(0,0,1,0.5))
points(HR_comma_sep$average_montly_hours[HR_comma_sep$left==1],HR_comma_sep$last_evaluation[HR_comma_sep$left==1],col=rgb(1,0,0,0.5))
legend("bottomright", c("Not Left","Left"),pch=c(1,1),col=c(rgb(0,0,1,0.5), rgb(1,0,0,0.5)))

library("lattice") #Load the `Lattice' graphics package
HR_subset<-subset(as.data.frame(HR_comma_sep),select=c('average_montly_hours', 'last_evaluation', 'satisfaction_level', 'left'))
super.sym <- trellis.par.get("superpose.symbol") #Get Symbol Plotting Information
splom(~HR_subset[1:3],groups=left,data = HR_subset,varnames=c("Average \nMonthly \nHours","Last \nEvaluation","Satisfaction \nLevel"),
      key = list(title = "Scatterplot Matrix",
                 columns = 2, 
                 points = list(pch = super.sym$pch[1:2],
                 col = super.sym$col[1:2]),
                 text = list(c("Not Left", "Left"))))

# Explore number of projects and left

# Create multiple figure
par(mfrow=c(3,2))

# Plot properties
label1 <- 'Number of Projects Completed'
label2 <- 'Left'
xBreaks <- c(seq(0, 7, length=8))
red <- rgb(1,0,0,0.5)
blue <- rgb(0,0,1,0.5)

# Table for mosaic
project_table <- table(HR_comma_sep$number_project, HR_comma_sep$left)

# mosaic
mosaicplot(project_table, main="Mosaic Plot of Left by Projects", xlab=label1, ylab=label2, las=2)

# boxplot
boxplot(HR_comma_sep$number_project~HR_comma_sep$left, xlab=label2, ylab=label1, main='Boxplot of Left by Projects')

# histogram - frequency
hist(HR_comma_sep$number_project[HR_comma_sep$left==1], col=red, freq=TRUE, breaks=xBreaks, ylim=c(0,4500),
    main='Histogram for Number of Projects by Left', cex.main=0.9, xlab=label1)
hist(HR_comma_sep$number_project[HR_comma_sep$left==0], add=TRUE, col=blue, freq=TRUE, breaks=xBreaks, cex.main=0.9)
legend('topright', c('Left', 'Not Left'), fill=c(red, blue))

# histogram - density
hist(HR_comma_sep$number_project[HR_comma_sep$left==1], col=red, freq=FALSE, breaks=xBreaks,
    main='Histogram for Number of Projects by Left', cex.main=0.9, xlab=label1)
hist(HR_comma_sep$number_project[HR_comma_sep$left==0], add=TRUE, col=blue, freq=FALSE, breaks=xBreaks, 
     cex.main=0.9)
legend('topright', c('Left', 'Not Left'), fill=c(red, blue))

# Empircal Cumulative Distribution 
E0 <- ecdf(HR_comma_sep$number_project[HR_comma_sep$left==0])
E1 <- ecdf(HR_comma_sep$number_project[HR_comma_sep$left==1])
plot(E0, col=blue, verticals=TRUE, do.points=FALSE, main='ECDF for Projects by Left', xlab=label1)
plot(E1, col=red, verticals=TRUE, do.points=FALSE, add=TRUE)
legend('bottomright', c('Not Left', 'Left'),lwd=1, lty=c(1,1), col=c(blue,red))

# Let's look at projects completed by time at company
plot(HR_comma_sep$time_spend_company[HR_comma_sep$left==0],HR_comma_sep$number_project[HR_comma_sep$left==0], 
     col=blue, main='Scatter plot for Time Spent at Company vs \n Projects Completed', cex.main=0.8,
    xlab='Time at Company (years)', ylab='Number of Projects Completed', ylim=c(0,8), xlim=c(0,10))
points(HR_comma_sep$time_spend_company[HR_comma_sep$left==1],HR_comma_sep$number_project[HR_comma_sep$left==1],
      col=red, pch=2)
legend('topright', c('Not Left', 'Left'), pch=c(1,2), col=c(blue,red), cex=0.5)
grid()

# Get subset
best_and_exp <- subset(HR_comma_sep, last_evaluation>=0.8 & time_spend_company>=4) # Best and Most Experienced

# Summary
summary(best_and_exp)

best_and_exp

# Make scatterplot matrix
library('lattice')
key_columns <- subset(as.data.frame(best_and_exp), select=c('satisfaction_level', 'number_project', 'average_montly_hours','time_spend_company', 'left'))
super.sym <- trellis.par.get("superpose.symbol") #Get Symbol Plotting Information
splom(~key_columns[1:4],groups=left,data = key_columns,varnames=c("Satisfaction \nLevel", 'Number of \nProjects', "Average \nMonthly \nHours", 'Time \nSpent at \nCompany'),
      key = list(title = "Scatterplot Matrix",
                 columns = 2, 
                 points = list(pch = super.sym$pch[1:2],
                 col = super.sym$col[1:2]),
                 text = list(c("Not Left", "Left"))))

# Left compared with promotion
comp_table <- table(best_and_exp$promotion_last_5years, best_and_exp$left)
mosaicplot(comp_table, main='Mosaic Plot of Left and if Received Promotion', xlab='Promotion Last 5 years', ylab='Left')


height_data<-rnorm(200, mean = 174.46, sd = 7.15) 
hist(height_data,col=rgb(0,0,1,0.5),main="Histogram for Synthetic Height Data", xlab="Height (cm)")
summary(height_data)

height_data_out<-height_data
height_data_out[1:10]<-height_data_out[1:10]*0.3937007874
hist(height_data_out,col=rgb(0,0,1,0.5),main="Histogram for Synthetic Height Data (with Unusual Obs.)", xlab="Height (cm)")
summary(height_data_out)

hdo_box<-boxplot(height_data_out,main="Boxplot of Synthetic Height Data (with Unusual Obs.)", ylab="Height (cm)")

hdo_box$out

library("readr")
fheight<-read_csv("./PearsonFather.csv",col_names="fheight",col_types="d")
sheight<-read_csv("./PearsonSon.csv",col_names="sheight",col_types="d")
fs_height<-data.frame(fheight,sheight)
plot(fs_height$fheight,fs_height$sheight,main="Father and Son Heights", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
summary(fs_height)

fheight_MCAR<-fheight
fheight_MCAR[rbinom(nrow(fheight),1,0.1)==1,]<-NA
sheight_MCAR<-sheight
sheight_MCAR[rbinom(nrow(sheight),1,0.1)==1,]<-NA
fs_height_MCAR<-data.frame(fheight_MCAR,sheight_MCAR)

plot(fs_height_MCAR$fheight,fs_height_MCAR$sheight,main="Father and Son Heights (MCAR)", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
summary(fs_height_MCAR)

library("mice")
imp_mean<-mice(fs_height_MCAR,method="mean",m=1,maxit=1)
fsh_mean_imp<-complete(imp_mean,1)
fsh_mean_imp$mis<-!complete.cases(fs_height_MCAR)
plot(fsh_mean_imp$fheight[fsh_mean_imp$mis==FALSE],fsh_mean_imp$sheight[fsh_mean_imp$mis==FALSE],main="Father and Son Heights (MCAR)", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
points(fsh_mean_imp$fheight[fsh_mean_imp$mis==TRUE],fsh_mean_imp$sheight[fsh_mean_imp$mis==TRUE],col=rgb(0.1,0.7,1,0.5))
legend("bottomright", c("Complete Cases","Imputed Cases"),pch=c(1,1),col=c(rgb(1,0.3,0.1,0.5), rgb(0.1,0.7,1,0.5)))

as.data.frame(lapply(fs_height,sd)) # Source Data Standard Deviations
as.data.frame(lapply(fs_height_MCAR,sd,na.rm=TRUE)) # Complete-case MCAR Data Standard Deviations
as.data.frame(lapply(fsh_mean_imp[1:2],sd,na.rm=TRUE)) # Mean-imputed MCAR Data Standard Deviations

imp_linreg<-mice(fs_height_MCAR,method="norm.nob",m=1)
fsh_linreg_imp<-complete(imp_linreg,1)
fsh_linreg_imp$mis<-!complete.cases(fs_height_MCAR)
plot(fsh_linreg_imp$fheight[fsh_linreg_imp$mis==FALSE],fsh_linreg_imp$sheight[fsh_linreg_imp$mis==FALSE],main="Father and Son Heights (MCAR)", xlab="Father Heights (in)",ylab="Son Heights (in)",col=rgb(1,0.3,0.1,0.5))
points(fsh_linreg_imp$fheight[fsh_linreg_imp$mis==TRUE],fsh_linreg_imp$sheight[fsh_linreg_imp$mis==TRUE],col=rgb(0.1,0.7,1,0.5))
legend("bottomright", c("Complete Cases","Imputed Cases"),pch=c(1,1),col=c(rgb(1,0.3,0.1,0.5), rgb(0.1,0.7,1,0.5)))

fit_all<-with(fs_height,lm(sheight~fheight))

fit_MCAR<-with(fs_height_MCAR,lm(sheight~fheight))

mimp_linreg<-mice(fs_height_MCAR,method="norm.nob",m=10)
fit_linreg_mimp<-with(mimp_linreg,lm(sheight~fheight))


summary(fit_all)
summary(fit_MCAR)
summary(pool(fit_linreg_mimp))

# Imputation by random sampling
imp_random<-mice(fs_height_MCAR, method='sample', m=1)
fsh_random<-complete(imp_random,1) # grab imputed values
fsh_random$mis<-!complete.cases(fs_height_MCAR) # create binary flag

# plot colours
orange = col=rgb(1,0.3,0.1,0.5)
blue = rgb(0.1,0.7,1,0.5)

# Plot data
plot(fsh_random$fheight[fsh_random$mis==FALSE], fsh_random$sheight[fsh_random$mis==FALSE], col=orange,
    main="Father and Son Heights (MCAR)", xlab='Father', ylab='Son')
points(fsh_random$fheight[fsh_random$mis==TRUE], fsh_random$sheight[fsh_random$mis==TRUE], col=blue)
points(fsh_linreg_imp$fheight[fsh_linreg_imp$mis==TRUE],fsh_linreg_imp$sheight[fsh_linreg_imp$mis==TRUE], col='green')
legend('bottomright', c('Complete Cases', 'Random Imputed Cases', 'Linear Regression Imputed Cases'), 
       pch=c(1,1,1), col=c(orange,blue,'green'), cex=0.7)

library("tm") # Text mining library
library("wordcloud") # Wordcloud plotting library
ulysses_raw<-readLines("./pg1727.txt")
ulysses_raw<-ulysses_raw[342:10599] # Strip out front and back matter
ulysses<-Corpus(VectorSource(ulysses_raw)) # Convert to corpus format
inspect(ulysses[1:30]) # Inspect first 30 lines

ulysses <- tm_map(ulysses, content_transformer(tolower)) # Convert corpus to lower case
ulysses <- tm_map(ulysses, removePunctuation) # Strip common punctuation
ulysses <- tm_map(ulysses, removeNumbers) # Strip numbers 
ulysses <- tm_map(ulysses, removeWords, stopwords("english")) # Strip default stop words

# Strip custom stop words
ulysses <- tm_map(ulysses, removeWords, c("i","and","are","it","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii","xiii","xiv","xv","xvi","xvii","xviii","xix","xx","xxi","xxii","xxiii","xxiv","xxv")) 

ulysses <- tm_map(ulysses, stripWhitespace) # Strip excess whitespace

inspect(ulysses[1:30]) # Inspect first 30 lines

ulysses_tdm <- TermDocumentMatrix(ulysses) # Create a table counting word occurences by corpus
ulysses_tdm_sparse<-removeSparseTerms(ulysses_tdm , 0.995) # Keep only words that appear more than (1-0.995)*10258 (around 51) times

ulysses_tdms_matrix <- as.matrix(ulysses_tdm_sparse) # Convert to matrix for processing
ulysses_tdms_freqs <- sort(rowSums(ulysses_tdms_matrix),decreasing=TRUE) # Compute frequencies and sort
ulysses_tdms_freqs_df <- data.frame(terms = names(ulysses_tdms_freqs),freq=ulysses_tdms_freqs) # Construct data frame
head(ulysses_tdms_freqs_df, 5) # Inspect the top 5 words

set.seed(8888)
wordcloud(words = ulysses_tdms_freqs_df$terms, freq = ulysses_tdms_freqs_df$freq, min.freq = 1,max.words=100, random.order=FALSE, random.color=FALSE, rot.per=0.4,colors=brewer.pal(8, "Dark2"))
