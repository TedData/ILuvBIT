import pandas as pd 
import numpy as np
#import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

np.random.seed(len(df))

N = 50
desk = 0
CI = []
while True:
    desk += 1 
    desks = []
    wait = []
    count = []
    count_N = []
    time=[]
    for i in range(desk):
        desks.append([])
    T = 3000
    t=0
    while t <= T:
        row = np.random.randint(len(df))
        t += df.loc[row].values[0]
        time.append(t)
        for i in range(desk):
            if desks[i]:
                desks[i][0] -= df.loc[row].values[0]
                while desks[i][0] <= 0:
                    if desks[i][1:]:
                        desks[i][1] += desks[i][0]
                        desks[i] = desks[i][1:]
                    elif not desks[i][1:]:
                        desks[i] = desks[i][1:]
                        break

        for i in range(len(desks)): 
            least = i 
            for k in range(i+1, len(desks)):
                if len(desks[k]) < len(desks[least]):
                    least = k
            desks[least], desks[i] = desks[i], desks[least]

        desks[0].append(df.loc[row].values[1])
        wait.append(sum(desks[0][:-1])) 
        
    index = (len(wait) * 3) // 10
    wait = wait[index:]
    time= time[index:]
    
    
    for i in range(len(wait)):
        if wait[i] > 8:
            count.append(0)
        elif wait[i] <= 8:
            count.append(1)
    
    for i in range(N):
        count_N.append(np.mean(count[(0+i*len(count)//50):(len(count)//50)*(i+1)]))
    
    count_N_mean = np.mean(count_N)
    count_N_std = np.std(count_N)
    CI.append([count_N_mean-1.96*count_N_std/len(count_N)**0.5, count_N_mean+1.96*count_N_std/len(count_N)**0.5])
       
    
    
    '''    
    if desk==7:
        for i in range(desk):
            print(len(desks[i]))
            print('*'*20)
        print(sum(wait)/len(wait))
        break'''
    
    if CI[desk-1][0] > 0.9:
        print(desk)
        break
    
#plt.plot(time, wait,'.')
#plt.axhline(y=8, color='r', linestyle='-')

#plt.show()