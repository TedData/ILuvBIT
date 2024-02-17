# twoSampleTtest.py
import numpy as np
from scipy.stats import ttest_ind

Treatment = np.array([94, 197, 16, 38, 99, 141, 23])
Control = np.array([52, 104, 146, 10, 51, 30, 40, 27, 46])

onesample_results  = ttest_ind(Treatment, Control)
print("sample means=(",np.mean(Treatment),",", np.mean(Control) ,")",
      " t = ", onesample_results[0], ", p-val = ", onesample_results[1])