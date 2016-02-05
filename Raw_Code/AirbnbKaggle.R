train = read.csv("train_users_2.csv",header=T,na.strings=c("","NA"))
##na.strings=c("","NA") is very very important, changes your blank cell to NA
test = read.csv("test_users.csv", header = T,na.strings=c("","NA"))
dim(train) #213451     16
dim(test)# 62096    15
users = rbind(train[1:15], test)
#drop id
users$id <- NULL
head(users)
#dealing with missing value 
users$gender = as.character(users$gender)
users$gender[users$gender=="-unknown-"] = "NA"
colnames(users)
for (i in 1:15) {
  print(sum(is.na(users[i]))/length(users)*100)
}
