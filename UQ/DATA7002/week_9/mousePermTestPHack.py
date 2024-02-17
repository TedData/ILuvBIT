# mousePermTestPHack.py
import numpy as np

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


Treatment = np.array([94, 197, 16, 38, 99, 141, 23])
Control = np.array([52, 104, 146, 10, 51, 30, 40, 27, 46])
t_obs = np.abs(np.mean(Treatment) - np.mean(Control))
PermTest(Treatment, Control)

# The management feels that the variance in the Treatment group
# is too big. Using small adjustments, we repet the experiment to obtain

Treatment2 = np.array([73, 69, 115, 110, 90, 75, 80, 100, 77,83, 68,97])
t_obs2 = np.abs(np.mean(Treatment2) - np.mean(Control))

print("The new differences in the observed statistic is ",t_obs2-t_obs)

PermTest(Treatment2, Control)
