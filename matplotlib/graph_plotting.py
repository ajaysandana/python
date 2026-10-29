import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025])
y1 = np.array([100, 180, 200])
y2 = np.array([150, 160, 190])

# marker is point which shows the data points
# markersize is the size of the marker

line_style = dict(marker='o', 
         markersize=8, 
         markerfacecolor='black', 
         markeredgecolor='white',
         linestyle='solid',
         linewidth=2
        )

# if we want to keep the color different for all the graphs, then pass the color parameter separately

plt.plot(x,y1, **line_style, color='black')
plt.plot(x,y2, **line_style, color='blue')

plt.show()