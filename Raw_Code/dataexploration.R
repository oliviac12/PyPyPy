data <- read.csv("f_DFF.csv", header = TRUE)
library(ggplot2)
#--------------
# Create Theme
#--------------

# BASIC THEME
theme.car_chart <- 
  theme(legend.position = "none") +
  theme(plot.title = element_text(size=14, family="Trebuchet MS", face="bold", hjust=0, color="#666666")) +
  theme(axis.title = element_text(size=14, family="Trebuchet MS", face="bold", color="#666666")) +
  theme(axis.title.y = element_text(angle=0)) 


# SCATTERPLOT THEME
theme.car_chart_SCATTER <- theme.car_chart +
  theme(axis.title.x = element_text(hjust=0, vjust=-.5))

# HISTOGRAM THEME
theme.car_chart_HIST <- theme.car_chart +
  theme(axis.title.x = element_text(hjust=0, vjust=-.5))

# SMALL MULTIPLE THEME
theme.car_chart_SMALLM <- theme.car_chart +
  theme(panel.grid.minor = element_blank()) +
  theme(strip.text.x = element_text(size=16, family="Trebuchet MS", face="bold", color="#666666"))    

#Program Type

ggplot(data=data, aes(x=Program)) + geom_histogram(fill="#880011")
            
# Program Type and Production? 
ggplot(data,aes(x=Program, y=Production.Ratio)) + geom_boxplot() 

small = subset(data, Program == 'Small Commercial (< 10 kW) and All Residential')
large = subset(data, Program == 'Large Commercial (>= 10 kW)')
summary(small$Production.Ratio)
summary(large$Production.Ratio)
summary(data[10:11])
#------------------------
# Histogram of production
#------------------------

ggplot(data=data, aes(x=Production.Ratio)) +
  geom_histogram(fill="#880011") +  
  ggtitle("Histogram of Production.Ratio") +
  labs(x="Production.Ratio", y="Count") + 
  theme.car_chart_HIST

#------------------------
# Dentisy of Production.Ratio
#------------------------


ggplot(data, aes(x=Program.Administrator, y=Production.Ratio)) +
       geom_boxplot()


#-------------------------
# Production Ratio and Rain/Snow?
#-------------------------

ggplot(data=data, aes(x=TST, y=Production.Ratio)) +
  geom_point(alpha=.4, size=4, color="#880011") +
  ggtitle("Production Ratio vs. Rain") +
  labs(x="Rain, inches to hundredths", y="Production Ratio,\n kwh/kw") +
  theme.car_chart_SCATTER

ggplot(data=data, aes(x=TSNW, y=Production.Ratio)) +
  geom_point(alpha=.4, size=4, color="#880011") +
  ggtitle("Production Ratio vs. Snow") +
  labs(x="Rain, inches to tenths", y="Production Ratio,\n kwh/kw") +
  theme.car_chart_SCATTER

ggplot(data=data, aes(x=Total.Cost, y=Production.Ratio)) +
  geom_point(alpha=.4, size=4, color="#880011") +
  ggtitle("Production Ratio vs. Cost") +
  labs(x="Cost", y="Production Ratio,\n kwh/kw") +
  theme.car_chart_SCATTER

ggplot(data=data, aes(x=MNTM, y=Production.Ratio)) +
  geom_point(alpha=.4, size=4, color="#880011") +
  ggtitle("Production Ratio vs. Temperature") +
  labs(x="Monthly Average Temperature", y="Production Ratio,\n kwh/kw") +
  theme.car_chart_SCATTER

ggplot(data=data, aes(x=Failure_Rate, y=Production.Ratio)) +
  geom_point(alpha=.4, size=4, color="#880011") +
  ggtitle("Production Ratio vs. Failure Rate") +
  labs(x="Failure Rate (%)", y="Production Ratio,\n kwh/kw") +
  theme.car_chart_SCATTER

ggplot(data=data, aes(x=MNTM, y=Production.Ratio)) +
  geom_point(aes(color=Program.Administrator)) +
  theme_bw()

require(GGally)
p <- ggpairs(data[c(6,11,16,20,21)],upper = "blank")
p
pairs(data[c(6,11,16,20,21)])

ggplot(data, aes(x=Program.Administrator, y=Production.Ratio, fill=Program.Administrator)) +
  geom_boxplot()

