from sklearn.datasets import make_blobs
from sklearn.metrics import zero_one_loss
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier

X_train, y_train = make_blobs(n_samples=1000, n_features=10, centers=3, random_state=10, cluster_std=5)

#Answer:
gammas = [0.1, 0.3, 0.5, 0.7, 1]
for gamma in gammas:
    GBC = GradientBoostingClassifier(learning_rate=gamma, n_estimators = 150)
    GBC.fit(X_train, y_train)
    plt.plot(np.arange(1,151,1), GBC.train_score_, label = gamma)
plt.legend()
plt.show()
