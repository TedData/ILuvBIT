import os
#print(os.getcwd())#显示当前路径
os.chdir('/Users/Ted/Desktop/computer_science/DATA7202/assessment_2')#更改路径，''里面为更改的路径
#print(os.getcwd())#显示当前路径


import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("ships.csv")

Y = df.damage
X = df.drop(['damage'], axis = 1)

model = sm.GLM(Y, X, family = sm.families.Poisson())

results = model.fit()
print(results.summary())