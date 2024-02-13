import numpy as np
import pandas as pd
import statsmodels.api as sm

X1 = np.array([0,1,2,3,4])
y = np.array([1,2,3,2,1])
X0_1 = np.zeros(5)
X0_2 = np.ones(5)

data_1 = np.array([X0_1,X1,y]).T
model_1 = pd.DataFrame(data_1,columns=['X0','X1','Y'])

data_2 = np.array([X0_2,X1,y]).T
model_2 = pd.DataFrame(data_2,columns=['X0','X1','Y'])

#linear model without intercept
lin_reg_1 = sm.OLS(model_1[['Y']].values.reshape(-1,), model_1[['X0','X1']]).fit() 
print('Model 1')
print(lin_reg_1.summary())
y_hat_1 = lin_reg_1.predict(model_1[['X0','X1']])
y_test = model_1[['Y']].values.reshape(-1,)
print("Model1 mean squared error loss: ", np.mean(np.power((y_test- y_hat_1).values,2)))
print("Model1 mean squared absolute error loss: ", np.mean(np.power(abs(y_test- y_hat_1).values,1)))
print("Model1 mean squared L1.5 loss: ", np.mean(np.power(abs(y_test- y_hat_1).values,1.5)))

#linear model with intercept
lin_reg_2 = sm.OLS(model_2[['Y']].values.reshape(-1,), model_2[['X0','X1']]).fit() 
print('*'*78)
print('Model 2')
print(lin_reg_2.summary())
y_hat_2 = lin_reg_2.predict(model_2[['X0','X1']])
y_test = model_2[['Y']].values.reshape(-1,)
print("Model1 mean squared error loss: ", np.mean(np.power((y_test- y_hat_2).values,2)))
print("Model1 mean squared absolute error loss: ", np.mean(np.power(abs(y_test- y_hat_2).values,1)))
print("Model1 mean squared L1.5 loss: ", np.mean(np.power(abs(y_test- y_hat_2).values,1.5)))

