#coins1.py
import numpy as np
from numpy.random import randint
from scipy import stats
import pandas as pd

np.random.seed(12345)

color = ['Purple', 'Brown', 'Pink', 'Blue', 'Teal', 
        'Salmon', 'Red', 'Turquoise', 'Magenta', 'Yellow', 
        'Tan', 'Green',  'Grey',  'Cyan',  'Mauve',
        'Beige', 'Lilac', 'Black', 'Peach', 'Orange']

# number of experiments
n = 100 


df = pd.DataFrame(index=color)
for col in color:
    result = randint(0,1+1,n)
    df.loc[col,'Heads'] = np.sum(result)
  
tmp = df[df["Heads"]==max(df["Heads"])]
      
num_heads = tmp.values[0][0]

# 1-cdf
p_value = stats.binom(100, 1/2).sf(num_heads)

print("p-value = ",p_value)
