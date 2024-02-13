import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression

x1 = np.array([0,1,2,3,4])
y = np.array([1,2,3,2,1])
data = np.array([x1,y]).T
model = pd.DataFrame(data,columns=['x1','y'])
X = model[['x1']]
Y = model[['y']]

#linear model without intercept
lin_reg_1 = LinearRegression(fit_intercept = False)
lin_reg_1.fit(X,Y)
print('beta_0: ',lin_reg_1.intercept_)
print('beta_1: ',float(lin_reg_1.coef_))
print('*'*20)

#linear model with intercept
lin_reg_2 = LinearRegression(fit_intercept = True)
lin_reg_2.fit(X,Y)
print('beta_0: ',float(lin_reg_2.intercept_))
print('beta_1: ',float(lin_reg_2.coef_))

print('*'*20)
y_hat_1 = lin_reg_1.predict(X)
print("Model1 mean squared error loss: ", np.mean(np.power((Y- y_hat_1).values,2)))
print("Model1 mean squared absolute error loss: ", np.mean(np.power(abs(Y- y_hat_1).values,1)))
print("Model1 mean squared L1.5 loss: ", np.mean(np.power(abs(Y- y_hat_1).values,1.5)))

print('*'*20)
y_hat_2 = lin_reg_2.predict(X)
print("Model2 mean squared error loss: ", np.mean(np.power((Y- y_hat_2).values,2)))
print("Model2 mean squared absolute error loss: ", np.mean(np.power(abs(Y- y_hat_2).values,1)))
print("Model2 mean squared L1.5 loss: ", np.mean(np.power(abs(Y- y_hat_2).values,1.5)))
