import numpy as np
from statsmodels.graphics.regressionplots import plot_leverage_resid2
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('softdrink.csv')
Y = df.Time
X = df.drop(['Time'], axis = 1)

#(a)
results = smf.ols('Time ~ Cases + Distance', data=df).fit()
print(results.summary())
K = 2
dfd = len(Y) - K - 1
yhat = results.predict(X).values
se = np.sqrt(np.sum((np.array(Y) - yhat) ** 2) / (dfd))
print('The standard error of estimate: ',se)


#(b)
results_his = results
sns.residplot(df.Cases, results.resid, lowess=False, color="g")
sns.residplot(df.Distance, results.resid, lowess=False, color="g")
sns.distplot(results.resid)
plt.show()
fig = sm.qqplot(results.resid)
plt.show()
sns.distplot(results_his.resid)
plt.show()


#(c)
fig, ax = plt.subplots(figsize=(8,6))
fig = plot_leverage_resid2(results, ax = ax)
