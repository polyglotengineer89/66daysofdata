#importing dataset
dataset = read.csv("Salary_Data.csv")

#splitting dataset into training set and test set
library(caTools)
set.seed(123)

split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set =subset(dataset, split=TRUE)
test_set = subset(dataset, split=FALSE)

#fitting simple linear regression to training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

#predict Test Result
y_pred = predict(regressor, newdata = test_set)


#Visualising Training set result
install.packages('ggplot2')
Library(ggplot2)

ggplot() + geom_point(aes(x=training_set$YearsExperience, y = training_set$Salary),
                      colour = 'red') + 
          geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
                    color= 'blue') +
          ggtitle('Salary vs Expectation (Training set)') +
          xlab("Year of experience") +
          ylab('Salary')

#Visualising Test set Result
Library(ggplot2)

ggplot() + geom_point(aes(x=test_set$YearsExperience, y = test_set$Salary),
                      colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color= 'blue') +
  ggtitle('Salary vs Expectation (Test set)') +
  xlab("Year of experience") +
  ylab('Salary')