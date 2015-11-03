data <- read.csv("f_DFF.csv", header = TRUE)
lm <- lm(Specific_Yield ~as.factor(Program.Administrator) + as.factor(Program) + MNTM + TSNW + CSI.Project.Tilt + MTR, data = data)
summary(lm)


plot(density(data$Production.Ratio, na.rm))


library(shinyapps)
shinyapps::deployApp('~/Documents/Incubator2/incubator2.Rmd')
