# Zschool.py  
# try to change n and mu_sc to explore sensitivity
import numpy as np
from scipy.stats import norm

mu_0 = 100
scsd = 4
mu_sc = 101 
n = 40

IQschool = np.random.normal(mu_sc,scsd,n)
Zscore = (np.mean(IQschool) - mu_0)/(scsd/np.sqrt(len(IQschool)))
p_val  = 1-norm.cdf(Zscore)
print(Zscore, p_val)

