# tTestSchool.py
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import t

IQ =  [110,105,97,104,98,112,115,108,90]
# t-test
onesample_results = ttest_1samp(IQ, 100)
print("sample mean=",np.mean(IQ), " t = ", onesample_results[0], ", p-val = ", onesample_results[1])

# try t-test for another set
IQ2 =  [105,105,104,102,99,108,105,108,103]
# t-test
onesample_results = ttest_1samp(IQ2, 100)
print("sample mean=",np.mean(IQ2), " t = ", onesample_results[0], ", p-val = ", onesample_results[1])

