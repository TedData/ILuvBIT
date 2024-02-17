# BenfordLaw.py
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import chisquare

def first_n_digits(num, n):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def BenfordTest(data):   
    plt.hist(data,bins=10)
    plt.show()
    expected = np.zeros(9)
    observed = np.zeros(9)    
    for i in range(9):
        expected[i] = np.log10(1 + (1/(i+1)))
    
    for num in data: 
        digit = int(first_n_digits(num,1))
        observed[digit - 1] = observed[digit - 1]+1    
    expected = expected*len(data)    
    result = chisquare(observed,expected)
    print("statistic = ",result[0],  "p-value = ",result[1])
    
    
np.random.seed(54321)
n = 100

data = np.random.normal(100000,10000,n)
BenfordTest(data)
