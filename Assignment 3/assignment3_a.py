import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics

# load the boston dataset
data_boston= datasets.load_boston(return_X_y=False)

# defining feature matrix(X) and response vector(y)
X = data_boston.data
y = data_boston.target

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=1)

# creating a linear regression object
reg = linear_model.LinearRegression()

# training the model using the training sets
reg.fit(X_train, y_train)

# linear regression coefficients
print('Coefficients are: \n', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score is: {}'.format(reg.score(X_test, y_test)))


#Scatter Plot

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)

y_pred = lm.predict(X_test)

plt.scatter(y_test,y_pred )
plt.xlabel("Prices: ")
plt.ylabel("Predicted prices:")
plt.title("Prices vs Predicted prices")
plt.show()   #Ideally, the scatter plot should create a linear line. Since the model does not fit 100%, the scatter plot is not creating a linear line.


# plot for residual error

## setting plot style
plt.style.use('fivethirtyeight')

## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color="red", s=10, label='Train data')

## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color="blue", s=10, label='Test data')

## plotting line for zero residual error
plt.hlines(y=0, xmin=0, xmax=50, linewidth=2)

## plotting legend
plt.legend(loc='upper right')

## plot title
plt.title("Residual errors")

## function to show plot
plt.show()


