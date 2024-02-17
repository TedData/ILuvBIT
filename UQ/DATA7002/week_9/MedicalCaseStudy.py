#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:30:31 2019

@author: slava
"""

import numpy as np
from numpy.random import seed
from scipy.stats import friedmanchisquare
import matplotlib.pyplot as plt
# seed the random number generator
seed(1)

def CreateData(n,p):
    arr = np.zeros(n)
    for i in range(n):
        if(np.random.rand()<p):
            arr[i] = 1
    return arr

# sample size
n = 600

means = [0.25, 0.23, 0.27, 0.31, 0.28]


data1 = CreateData(n,means[0])
data2 = CreateData(n,means[1])
data3 = CreateData(n,means[2])
data4 = CreateData(n,means[3])
data5 = CreateData(n,means[4])

# plot
summaryMean = [np.mean(data1), np.mean(data2),np.mean(data3), \
           np.mean(data4),np.mean(data5)]

summaryStd = [np.std(data1), np.std(data2),np.std(data3), \
           np.std(data4),np.std(data5)]

summaryStd = summaryStd/np.sqrt(n)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(np.arange(5)+1, summaryMean, 0.35,
                color='black')

plt.xlabel("location")
plt.ylabel("infcetion percentage")

plt.xlabel("location")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)


ax.bar(np.arange(5)+1, summaryMean, 0.35,
                color='black',
                yerr=summaryStd,
                error_kw=dict(elinewidth=2,ecolor='red'))

plt.xlabel("location")
plt.ylabel("infcetion percentage")
plt.show()

stat, p = friedmanchisquare(data1, data2,data3,data4,data5)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')
    
    
    
    
    
    