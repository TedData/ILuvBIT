import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")
import os
#print(os.getcwd())#显示当前路径
os.chdir('/Users/Ted/Desktop/computer_science/DATA7202/assessment_1')#更改路径，''里面为更改的路径
#print(os.getcwd())#显示当前路径

#(a)
df = pd.read_csv('Hitters.csv')

for cname in df.columns:
    if(df[cname].dtype == 'object'):
        df[cname][df[cname] == "?"] = np.nan
df = df.dropna()

lb_make = LabelEncoder()
df.League = lb_make.fit_transform(df.League)
df.Division = lb_make.fit_transform(df.Division)
df.NewLeague = lb_make.fit_transform(df.NewLeague)
print(df.dtypes)

#(c)
model = LinearRegression()
Y = df.Salary
X = df.drop(['Salary'],axis=1)
mse = []
kf = KFold(n_splits=10, random_state=0)
kf.get_n_splits(X)

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
    y_train, y_test = Y.iloc[train_index], Y.iloc[test_index]
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    mse.append(mean_squared_error(y_test, y_pred))
    
print("linear regression cross validation error =", np.mean(mse))