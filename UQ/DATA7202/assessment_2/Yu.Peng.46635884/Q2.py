import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("ships.csv")

Y = df.damage
X = df.drop(['damage'], axis = 1)

model = sm.GLM(Y, X, family = sm.families.Poisson())
results = model.fit()
print(results.summary())