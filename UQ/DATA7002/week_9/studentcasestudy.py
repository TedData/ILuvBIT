# Student case study studentcasestudy.py

import numpy as np
import pandas as pd

def PermTest(Treatment, Control):
    t_obs = np.abs(np.mean(Treatment) - np.mean(Control))

    B = 10000
    
    combined = np.append(Treatment,Control)
    
    ell = np.zeros(B)
    
    for i in range(0,B):
       tmp =  np.random.permutation(combined)
       t_tmp = tmp[0:Treatment.shape[0]]
       c_tmp = tmp[Treatment.shape[0]:combined.shape[0]]
       dif =  np.abs(np.mean(t_tmp) - np.mean(c_tmp))
       if(dif>t_obs):
           ell[i]=1
           
    ell_mean = np.mean(ell)  
    ell_std  = np.std(ell)  
    print("p-val=",ell_mean, " p_value 95% CI = [",ell_mean - 1.96*ell_std/np.sqrt(B), 
                             " , ", ell_mean + 1.96*ell_std/np.sqrt(B),"]")  
    
# load data
ds = pd.read_csv("student_data.csv")

# create new dataset
df = ds[['gender','GPA']]

# set categorical type for gender
df.gender = df.gender.astype('category')
df.dtypes

#Plot the GPA as a function of gender
print("F")
print(df.GPA[df.gender=="F"].describe())
print("-----------------------------------------")
print("M")
print(df.GPA[df.gender=="M"].describe())
print("-----------------------------------------")

from seaborn import boxplot

boxplot(x="gender", y="GPA",  data=df, palette="Set3")

# 2-sample t-test
from scipy.stats import ttest_ind
group1 = df.GPA[df.gender=="F"].values
group2 = df.GPA[df.gender=="M"].values

twosample_results  = ttest_ind(group1, group2)
print("sample means=(",np.mean(group1),",", np.mean(group2) ,")",
      " t = ", twosample_results[0], ", p-val = ", twosample_results[1])

# permutation test
t_obs = np.abs(np.mean(group1) - np.mean(group2))
PermTest(group1, group2)