import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=100)
# print(scores)

plt.hist(scores, bins=10, color='red', edgecolor='black')


plt.show()