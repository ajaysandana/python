import matplotlib.pyplot as plt
import numpy as np

categories = ['Seniors', 'Managers', 'Juniors', 'staff']
values = np.array([25, 30, 35, 20])
colors = ['red', 'yellow', 'blue', 'green']

# autopct() -- this parameter is used to display the percentage values on the pie slices. 1.1f shows one decimal place
#explode() -- if we want to show a slice of piechart explode

plt.pie(values, labels=categories,
                colors=colors,
                autopct='%1.1f%%',
                explode=(0.1, 0, 0, 0),
                shadow=True,
                startangle=90)
plt.show()