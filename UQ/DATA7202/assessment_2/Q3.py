import os
#print(os.getcwd())#显示当前路径
os.chdir('/Users/Ted/Desktop/computer_science/DATA7202/assessment_2')#更改路径，''里面为更改的路径
#print(os.getcwd())#显示当前路径



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
#pd.plotting.scatter_matrix(df, alpha=1.0)
#plt.show()
results_his = results
sns.residplot(df.Cases, results.resid, lowess=False, color="g")
sns.residplot(df.Distance, results.resid, lowess=False, color="g")
sns.distplot(results.resid)
plt.show()
fig = sm.qqplot(results.resid)
plt.show()
sns.distplot(results_his.resid)
plt.show()

'''

fig = plt.figure()
x = results.resid
ax = fig.add_subplot(111)
ax.hist(x,color='blue',alpha=0.8,rwidth=0.9)
plt.title(u'The histogram of the residuals.')
plt.show()
'''

#(c)

fig, ax = plt.subplots(figsize=(8,6))
fig = plot_leverage_resid2(results, ax = ax)


