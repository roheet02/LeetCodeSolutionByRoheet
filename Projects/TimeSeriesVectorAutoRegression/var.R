#install.packages('readxl')
library(readxl)
data=read_excel('/Users/rohit/Desktop/Var data set.xlsx')


data1=data[-1]
View(data1)

# Load the ggplot2 library
library(ggplot2)

# Create separate plots for each time series using facet_wrap
ggplot(data, aes(x = date)) +
  geom_line(aes(y = rgnp), color = "blue", size = 1) +
  labs(title = "Real Gross National Product", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"rgnp", scales = "free_y")

ggplot(data, aes(x = date)) +
  geom_line(aes(y = pgnp), color = "red", size = 1) +
  labs(title = "Potential real GNP", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"pgnp", scales = "free_y")

ggplot(data, aes(x = date)) +
  geom_line(aes(y = ulc), color = "green", size = 1) +
  labs(title = "Unit labor cost", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"ulc", scales = "free_y")

# Repeat this pattern for each time series (e.g., gdfco, gdf, gdfim, gdfcf, gdfce)
ggplot(data, aes(x = date)) +
  geom_line(aes(y = gdfco), color = "purple", size = 1) +
  labs(title = "Fixed weight deflator for personal consumption expenditure excluding food and energy", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"gdfco", scales = "free_y")

ggplot(data, aes(x = date)) +
  geom_line(aes(y = gdf), color = "orange", size = 1) +
  labs(title = "Fixed weight GNP deflator", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"gdf", scales = "free_y")

ggplot(data, aes(x = date)) +
  geom_line(aes(y = gdfim), color = "pink", size = 1) +
  labs(title = "Fixed weight import deflator.", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"gdfim", scales = "free_y")



ggplot(data, aes(x = date)) +
  geom_line(aes(y = gdfcf), color = "brown", size = 1) +
  labs(title = "Fixed weight deflator for food in personal consumption expenditure", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"gdfcf", scales = "free_y")

ggplot(data, aes(x = date)) +
  geom_line(aes(y = gdfce), color = "black", size = 1) +
  labs(title = "Fixed weight deflator for energy in personal consumption expenditure", y = "Values", x = "Date") +
  theme_minimal() +
  facet_wrap(~"gdfce", scales = "free_y")


library(astsa)
par(mfrow = c(2, 2))
acf(data$rgnp)
pacf(data$rgnp)
acf(data$ulc)
pacf(data$ulc)
model1<-sarima(data$rgnp,p=2,d=0,q=2)

library(tseries)
adf_test<-adf.test(data$rgnp)
adf_test
adf_test<-adf.test(data$ulc)
adf_test

acf(data$rgnp)
pacf(data$rgnp)


acf(data$ulc)
pacf(data$ulc)

mydata<-data[c('rgnp','ulc')]
mydata


mydata1<-cbind(diff(mydata$rgnp),diff(mydata$ulc))
mydata1

#install.packages('vars')
library(vars)
max_lag <- 10  # Set a maximum number of lags to consider
lag_sel <- VARselect(mydata1, lag.max = max_lag, type= 'both')
print(lag_sel)
optimal_lag <- lag_sel$selection[1] 
optimal_lag

var_model<-VAR(mydata1,p=4,type = 'const')
var_model
summary(var_model)



forecast<-predict(var_model,n.ahead  = 25)
forecast
plot(forecast)

#install.packages("lmtest")

library(lmtest)
# Perform Granger causality test
granger_test_result <- grangertest(mydata$ulc ~ mydata$rgnp, order = 10, data =mydata)
summary(granger_test_result)
granger_test_result

granger_test_result <- grangertest(mydata$rgnp ~ mydata$ulc, order = 10, data =mydata)
summary(granger_test_result)
granger_test_result







