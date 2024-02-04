import os

os.chdir('/Users/Ted/Desktop/computer_science/INFS3200/assignment/dataset')

import pandas as pd
df = pd.read_csv("Book3.csv",header=None)

#(1)

m = []
for i in range(len(df)):
    if df[0].values[i] % 100 == 0:
        m.append(i)
print('There were {} records in the sample set.'.format(len(m)))
print(df.loc[m])
print('-'*50)


#(2)

df_new=df.loc[m]
null=pd.isnull(df_new).sum().sum()
print('There are {} fields that contain NULL.'.format(null))
print('-'*50)


#(3)

null=pd.isnull(df_new).sum().sum()
value=df_new.count().sum()
empo=null/(null+value)*1000000
print('The Empo is',empo)