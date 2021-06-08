from collections import Counter
import cleantext

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

alpha = " abcdefghijklmnopqrstuvwxyz"

with open("P.txt",'r') as f:
    
    c = f.readlines()
    p = cleantext.clean(c, all=True) 

ax = plt.axes(projection='3d')

for index, char in enumerate(p):
        
    counter_ = Counter(p)
    
#    print(char, counter_)

    x = index
    y = alpha.index(char.lower())
    z = counter_[char]
        
    ax.scatter(x, y, z, c = x, cmap = plt.cm.Spectral, norm = plt.Normalize(vmin=0, vmax=2000))
#    print(x,y,z)

x, y = np.meshgrid(x, y)


plt.set_cmap("Greens")
plt.show()
