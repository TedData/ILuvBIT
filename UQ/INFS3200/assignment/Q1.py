import os

os.chdir('/Users/Ted/Desktop/computer_science/INFS3200/assignment/dataset')

import pandas as pd


df = pd.read_csv("Book1.csv",header=None)

for i in range(len(df[2])):
    if not df[2].notna().values[i]:
        print('There is null value in authors for Book1')
        break
    if i==len(df[2])-1:
        print('There is no null value in authors for Book1')
m=0
for i in range(len(df[2])):
    for j in range(i+1, len(df[2])):
        if m==1:
            break
        if df[2].values[i]==df[2].values[j]:
            print('There is duplicate data in authors for Book1')
            m=1
    if m==1:
        break
if m==0:
    print('There is no duplicate data in authors for Book1')
