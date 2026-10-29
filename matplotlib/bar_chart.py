import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['A', 'B', 'C', 'D', 'E'])
values = np.array([25, 40, 30, 35, 20])

# plt.bar(categories, values, color='black') # to create a vertical bar chart

plt.barh(categories, values, color='black') #to create a horizontal bar chart
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('random bar chart')
plt.show()