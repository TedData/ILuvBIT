import os
#print(os.getcwd())#显示当前路径
os.chdir('/Users/Ted/Desktop/computer_science/DATA7202/assessment_2')#更改路径，''里面为更改的路径
#print(os.getcwd())#显示当前路径


import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.model_selection import KFold
from sklearn.metrics import zero_one_loss
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

from sklearn import model_selection, datasets
from sklearn.linear_model import LinearRegression, Lasso


import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('Hitters.csv')
for cname in df.columns:
    if(df[cname].dtype == 'object'):
        df[cname][df[cname] == "?"] = np.nan
df = df.dropna()
'''
lb_Hitters = LabelEncoder()
df.League = lb_Hitters.fit_transform(df.League)
df.Division = lb_Hitters.fit_transform(df.Division)
df.NewLeague = lb_Hitters.fit_transform(df.NewLeague)
df.Salary = lb_Hitters.fit_transform(df.Salary)
'''
lb_make = LabelEncoder()
df.League = lb_make.fit_transform(df.League)
df.Division = lb_make.fit_transform(df.Division)
df.NewLeague = lb_make.fit_transform(df.NewLeague)
df.Salary = lb_make.fit_transform(df.Salary)

Y = df.Salary
X = df.drop(['Salary'],axis=1)


n_points = 80 
# points
#X, Y =  make_friedman1(n_samples=n_points, n_features=5, 
                       #noise=0.5, random_state=100)















linreg = linear_model.LinearRegression()
linreg.fit(X,Y)
linreg.intercept_
linreg.coef_


scores = list()
scores_std = list()

lasso = linear_model.Lasso(fit_intercept=True, normalize = True)
alphas = np.logspace(-10, -.5, 30)

for alpha in alphas:
     lasso.alpha = alpha
     this_scores = -cross_val_score(lasso, X, Y,scoring='neg_mean_squared_error',cv=5)
     scores.append(np.mean(this_scores))
     scores_std.append(np.std(this_scores))
    

plt.plot(alphas, scores)
# plot error lines showing +/- std. errors of the scores
plt.plot(alphas, np.array(scores) + np.array(scores_std) / np.sqrt(len(X)),
              'b--')
plt.plot(alphas, np.array(scores) - np.array(scores_std) / np.sqrt(len(Y)),
              'b--')
plt.ylabel('CV score (mean squared error)')
plt.xlabel('lambda')
plt.axhline(np.max(scores), linestyle='--', color='.5')

lasso = linear_model.Lasso(fit_intercept=True,alpha=0.9)
lasso.fit(X,Y)
lasso.coef_
lasso.intercept_


