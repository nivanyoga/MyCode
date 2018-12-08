#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sympy as sp
import numpy as np

from sympy import *
x=sp.Symbol('x')
init_printing(pretty_print=True)

def y(x):
    return (10*x**3 + 1/2*x**2 + 10) 

p=sp.diff(y(x))
print (p)
p=sp.diff(y(x), x, 2)
print (p)

p=sp.diff(y(x), x, 3)
print (p)


# In[ ]:




