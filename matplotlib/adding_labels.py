import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025])
y1 = np.array([100, 180, 200])
y2 = np.array([150, 160, 190])

plt.title("sales data", fontsize=16, fontweight='bold', family = 'times new roman', color='black')

plt.xlabel("year", fontsize=20, fontweight='bold', family = 'times new roman', color='green')

plt.ylabel("sales", fontsize=20, fontweight='bold', family = 'times new roman', color='blue')

plt.xticks(x)  # Set the x-axis tick positions that mean it will show the actual years

plt.tick_params(axis='both', labelsize=12, labelcolor='black')

plt.plot(x,y1)
plt.plot(x,y2)
plt.subplots_adjust(left=0.2,   # this creates space on the left for the y-axis labels
                    bottom=0.2) #this creates space at the bottom for the x-axis labels
plt.show()
