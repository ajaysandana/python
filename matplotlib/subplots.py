import matplotlib.pyplot as plt
import numpy as np

# print(plt.subplots(2,2))

# the subplots returns a tuple which has the figure and axes
# (<Figure size 640x480 with 4 Axes>, array([[<Axes: >, <Axes: >],
#        [<Axes: >, <Axes: >]], dtype=object))

# figure - entire canvas
# axes = a subplot(single plot). this is numpy array

x=np.array([1,2,3,4,5])

# x=[1,2,3,4,5]
# x*2=[1,2,3,4,5,1,2,3,4,5] this is how the python list will look with x multiplied by 2
# this is the reason we got the error 'x and y must have same first dimension, but have shapes (5,) and (10,)'
#  but for numpy arrays x*2 = [2,4,6,8,10] and the x and y have the same shape and dimensions

figure, axes = plt.subplots(2,2)

#axes[0,0] signifies the first row and first column plot out of the 2,2 plot
axes[0,0].plot(x, x*2, color='red')
axes[0,0].set_title('x*2')

axes[0,1].plot(x, x*3, color='blue')
axes[0,1].set_title('x*3')

axes[1,0].plot(x, x*4, color='green')
axes[1,0].set_title('x*4')

axes[1,1].plot(x, x*5, color='orange')
axes[1,1].set_title('x*5')
# plt.subplots_adjust(wspace=0.3, hspace=0.3)
plt.tight_layout()

plt.show()