
# Place your answer here (Sample Solution)

clean1 = read.csv("datasets/unclean1.csv", header=FALSE)
d1 = read.csv("datasets/iris1.csv", header=TRUE)

# strings are imported as factors in R version 3. You can cast it to character in each question, or alternatively
# add stringsAsFactors=FALSE parameter to read.csv -- as mentioned in Piazza instruction.
# the sample solution follows the Piazza instructions method

clean1 = read.csv("datasets/unclean1.csv", header=FALSE, stringsAsFactors=FALSE)
d1 = read.csv("datasets/iris1.csv", header=TRUE, stringsAsFactors=FALSE)

# Place your answer here
colnames(clean1) = clean1[ nrow(clean1) ,  ]
clean1 = clean1[ -nrow(clean1) ,  ]

# Place your answer here
datatype1 = d1
datatype1$Petal.Length = as.numeric(datatype1$Petal.Length)
datatype1$Sepal.Length = as.numeric(datatype1$Sepal.Length)
datatype1$Petal.Width = as.numeric(datatype1$Petal.Width)
datatype1$Sepal.Width = as.numeric(datatype1$Sepal.Width)
datatype1$Species = as.character(datatype1$Species)

# Place your answer here
sum_narm = mean(as.numeric(clean1$Petal.Width), na.rm=TRUE)

# Place your answer here
check1 = apply(!is.na(d1), 1, all) # can use other functions like complete.cases as well for NA
check2 = apply(d1!="", 1, all)

clean2 = d1[ check1 & check2 ,  ]

# Place your answer here
library("jsonlite")
iris3 = read_json("datasets/iris3.json", simplifyVector=TRUE)
iris4 = read.csv("datasets/iris4.csv", header=TRUE)

rbind1 = rbind(iris3, iris4)

# Place your answer here
select1 = d1[ c(1:5, (nrow(d1)-9) : nrow(d1)) ,  ]

# Place your answer here
select2 = d1
select2 = select2[ select2$Species!="versicolor" ,  ]

# Place your answer here
select3 = d1
select3 = select3[ select3$Species=="setosa" , "Petal.Length"  ] = 0

# Place your answer here
select2$Species = factor(select2$Species, levels=c("setosa","versicolor","virginica"))

temp1 = table(select2$Species)

count1 = as.vector(temp1)
names(count1) = names(temp1)

# Place your answer here
fun1 = function(x1, x2) {
    return( det(x1)+det(x2) )
}

# Place your answer here
sum1 = sum(d1$Petal.Length)

# Place your answer here
checknumeric = sapply(d1, is.numeric)
apply1 = apply(d1[,checknumeric], 2, function(x) sum(x) / median(x) )

# Place your answer here
agg1 = aggregate(. ~ Species, data = d1, sum)
row.names(agg1) = agg1$Species
agg1 = agg1[,c("Petal.Length","Petal.Width", "Sepal.Length", "Sepal.Width")]

# Place your answer here
source("script1.R")

# Place your answer here
fun1 = function(x1, x2) {
    return( list(x1, x2, det(x1)+det(x2)) )
}

# Place your answer here
lapply1 = sum( unlist( lapply(list1, function(x) if(is.matrix(x)) det(x) else NA) ), na.rm=TRUE ) 
sapply1 = sum( sapply(list1, function(x) if(is.matrix(x)) det(x) else NA), na.rm=TRUE )

# Place your answer here
for1 = 0
for(x in list1) {
    if(is.matrix(x)) {
        for1 = for1 + det(x)
    }
}

while1 = 0
ctr1 = length(list1)
while(ctr1 > 0 ) {
    if(is.matrix(list1[[ctr1]])) {
        while1 = while1 + det(list1[[ctr1]])
    }
    ctr1 = ctr1 - 1 ;
}


# Place your answer here
set.seed(55)
temp1 = sample(x=1:nrow(d1), size=80, replace=FALSE)
sample1 = d1[ temp1 ,  ]

set.seed(55)
temp1 = sample(x=1:nrow(d1), size=80, replace=TRUE)
sample2 = d1[ temp1 ,  ]

# Place your answer here
set.seed(55)
temp1 = sample(x=1:nrow(d1), size=80, replace=TRUE, prob= (1*(d1$Species=="setosa")) + (2*(d1$Species=="versicolor")) + (4*(d1$Species=="virginica")) )
sample3 = d1[ temp1 , ]

# Place your answer here
weighted_iterative = c()
for(i in 1:100) {
    set.seed(i)
    temp1 = sample(x=1:nrow(d1), size=80, replace=TRUE, prob= (1*(d1$Species=="setosa")) + (2*(d1$Species=="versicolor")) + (4*(d1$Species=="virginica")) )
    weighted_iterative = c(weighted_iterative, mean(d1[ temp1 , "Sepal.Length" ]))
}

# Place your answer here
set.seed(55)
temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="setosa"))
stratified_setosa = d1[ temp1 ,  ]

set.seed(55)
temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="versicolor"))
stratified_versicolor = d1[ temp1 ,  ]

set.seed(55)
temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="virginica"))
stratified_virginica = d1[ temp1 ,  ]

# Place your answer here
setosa_mean = c()
versicolor_mean = c()
virginica_mean = c()

for(i in 1:100) {

    set.seed(i)
    temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="setosa"))
    setosa_mean = c(setosa_mean, mean(d1[ temp1 , "Sepal.Length" ]))

    set.seed(i)
    temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="versicolor"))
    versicolor_mean = c(versicolor_mean, mean(d1[ temp1 , "Sepal.Length" ]))

    set.seed(i)
    temp1 = sample(x=1:nrow(d1), size=10, replace=TRUE, prob=1*(d1$Species=="virginica"))
    virginica_mean = c(virginica_mean, mean(d1[ temp1 , "Sepal.Length" ]))
    
}
