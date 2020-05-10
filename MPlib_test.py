import pandas as pd 
from matplotlib import pyplot as plt 
import math as mt
x = []
y = []
i = 1
while i <100:
    x.append(i/10)
    y.append(mt.sin(i/10))
    i+=1
plt.plot(x, y)
plt.show
