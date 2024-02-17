#coins2.py
import numpy as np
from numpy.random import randint
from scipy import stats
import pandas as pd

np.random.seed(12345)

N = 100000
ell = np.zeros(N)

for i in range(N):
    exp = np.random.binomial(100,0.5,20)
    if(max(exp)>=58):
        ell[i]=1
        
print(np.mean(ell))
