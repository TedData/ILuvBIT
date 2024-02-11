import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('Hitters.csv')
for cname in df.columns:
    if(df[cname].dtype == 'object'):
        df[cname][df[cname] == "?"] = np.nan
df = df.dropna()

lb_make = LabelEncoder()
df.League = lb_make.fit_transform(df.League)
df.Division = lb_make.fit_transform(df.Division)
df.NewLeague = lb_make.fit_transform(df.NewLeague)

Y = df.Salary
X = df.drop(['Salary'],axis=1)


#(a)

mse_min=[]
model = LinearRegression()
pca = PCA()
for i in range(1,20):
    pca.n_components = i
    mse = []
    X_pca = pca.fit_transform(X)
    mse = -model_selection.cross_val_score(model, X_pca, Y,scoring='neg_mean_squared_error',cv=10)
    mse_min.append(np.mean(mse))

print('The optimal number of components is '+ str(mse_min.index(min(mse_min))+1) + ". Linear regression cross validation error = "+ str(min(mse_min)))
print('-'*50)
plt.plot(range(1, len(mse_min) + 1), mse_min)
plt.xlabel('Number of principal components in regression')
plt.ylabel('MSE')
plt.title('Salary')
plt.axhline(np.min(mse_min), linestyle='--', color='.5')
plt.show()


#(b)

scores = list()
lasso = Lasso(fit_intercept=True)
alphas = np.arange(0,300,1)

for alpha in alphas:
     lasso.alpha = alpha
     this_scores = -model_selection.cross_val_score(lasso, X, Y,scoring='neg_mean_squared_error',cv=10)
     scores.append(np.mean(this_scores))
     
plt.plot(alphas, scores)
plt.ylabel('CV score (mean squared error)')
plt.xlabel('lambda')
plt.axhline(np.min(scores), linestyle='--', color='.5')
print('The best lambda is '+ str(alphas[scores.index(min(scores))]) + ". The corresponding mean squared error = "+ str(min(scores)))

