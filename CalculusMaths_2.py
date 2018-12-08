__author__ = 'DEFAULT'


import sympy as sp
import scipy as si
import numpy as np
import smtplib
import matplotlib.pyplot as plt

from si.integrate import quad

x = sp.Symbol('x')
y = sp.integrate(3.0*x**3+x**2+5,x)
print (y)


def f(y):
    return (3.0*x**3+x**2+5)


i=quad(f,0,2)

print (i)