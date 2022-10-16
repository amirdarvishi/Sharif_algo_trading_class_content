from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# define series
x = [0,1,2,3,4]
y = [0,2,4,6,8]

# plot first chart with -- style and blue color with * marker 
plt.plot(x,y, 'b*--', label = 'first')
# create second series
x2= np.arange(0,4.5,0.5)
# plot in 2 part, we use x^2 for y axis
plt.plot(x2[:3],x2[:3]**2, 'r', label='x^2')
plt.plot(x2[2:],x2[2:]**2, 'g', label='x^2')

# some styling stuff
plt.title('first chart', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
plt.xlabel('date')
plt.ylabel('price')
plt.xticks([0,1,2,3,4,5,9])
plt.legend()
# save image
plt.savefig('graph.png', dpi=300)
# show
plt.show()
