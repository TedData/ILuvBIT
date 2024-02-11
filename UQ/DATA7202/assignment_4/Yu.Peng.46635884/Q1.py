import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

np.random.seed(len(df))

N = 50
min_desk = -1
wait = []
result = [[],[],[]]

for desk in range(1, 16):
    desks = []
    count = []
    count_N = []
    T = 3000
    wait.append([])
    
    for i in range(desk):
        desks.append([])
    
    while T >= 0:
        row = np.random.randint(len(df))
        T -= df.loc[row].values[0]
        
        #Check whether the remaining service time of the first customer on each desk is negative. If so, delete his time and add the negative time to the service time of the next customer.
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

        #Find the desk with the smallest queue.
        #To be clear, I'm not looking for No. of desk with the smallest queue here, but I'm setting No. of desk with the smallest queue to be 0.
        for i in range(len(desks)):
            least = i 
            for k in range(i + 1, len(desks)):
                if len(desks[k]) < len(desks[least]):
                    least = k
            desks[least], desks[i] = desks[i], desks[least]

        #Obtain the wait time of the customer
        desks[0].append(df.loc[row].values[1])
        wait[desk - 1].append(sum(desks[0][:-1])) 
    
    #Discard the first 30% of the samples    
    index = (len(wait[desk - 1]) * 3) // 10
    wait[desk - 1] = wait[desk - 1][index:]
    
    #Gets the number of customers whose wait time is less than 8 minutes
    for i in range(len(wait[desk - 1])):
        if wait[desk - 1][i] > 8:
            count.append(0)
        elif wait[desk - 1][i] <= 8:
            count.append(1)

    #Using N = 50 batches to estimate the probability
    for i in range(N):
        count_N.append(np.mean(count[(0+i*len(count)//50):(len(count)//50)*(i+1)]))

    #The percentage of the number of customers meeting the conditions
    result[0].append(np.mean(count_N))

    #The minimum value of the confidence interval for this percentage
    result[1].append(np.mean(count_N) - 1.96 * np.std(count_N) / len(count_N) ** 0.5)
    
    #The maximum value of the confidence interval of this percentage
    result[2].append(np.mean(count_N) + 1.96 * np.std(count_N) / len(count_N) ** 0.5)

    #Find out the minimum number of desks that meet the topic condition
    if min_desk == -1:
        if result[1][desk-1] > 0.9:
            min_desk = desk

print('The minimum number of desks is {}.'.format(min_desk))
print('The mean of the percentage that meets the requirement = ',result[0][min_desk - 1])
print('The CI of the percentage that meets the requirement = (',result[1][min_desk - 1], ',',result[2][min_desk - 1],')')

plt.plot(range(1,16), result[0])
plt.plot(range(1,16), result[1], linestyle='--')
plt.plot(range(1,16), result[2], linestyle='--')
plt.xlabel('the number of desk')
plt.ylabel('Percentage of people waiting less than 8 minutes')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(wait[min_desk-1],color='blue',alpha=0.8,rwidth=0.9)
plt.xlabel('waiting time of the customer')
plt.ylabel('population')
plt.title(u"When dask = 7, the customer's waiting time.")
plt.show()

print('the mean of customer waiting time = ',np.mean(wait[min_desk-1]))
print('the CI of customer waiting time = (',np.mean(wait[min_desk-1])-1.96*np.std(wait[min_desk-1])/len(wait[min_desk-1])**0.5, ',',np.mean(wait[min_desk-1])+1.96*np.std(wait[min_desk-1])/len(wait[min_desk-1])**0.5,')')
