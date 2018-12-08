__author__ = 'DEFAULT'

import math as m
import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return x**3 - 3*x**2
    #return (x-2)**2

#We can call this function like any other function:

for x in [-3,-2,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(x, p(x))

X = np.linspace(-3, 9, 50, endpoint=True)
F = p(X)
plt.plot(X,F)
plt.show()
