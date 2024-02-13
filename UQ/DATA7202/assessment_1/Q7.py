import numpy as np 
N = 10000
np.random.seed(N)
ell = np.zeros(N)
for i in range(N):
    x = np.random.uniform(0,1)
    y = np.random.uniform(0,1)
    if(y < 1 / (x**2 + 2*x + 3)):
    	ell[i] = 1
ell_mean = np.mean(ell)
ell_std = np.std(ell)
print('mean = ',ell_mean,'CI = (',ell_mean-1.96*ell_std/N**0.5, ',',ell_mean+1.96*ell_std/N**0.5,')')
