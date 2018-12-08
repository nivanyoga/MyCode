__author__ = 'DEFAULT'


import os
import io
import fileinput
import math
import csv
import glob
import dateutil
import calendar
import smtplib
import numpy as np
import matplotlib.pyplot as plt


#mortgage=510000
#base_rate=2
#rate = base_rate + 2
#repay = 1000

#while (mortgage > 0):
 #   monthly = math.floor(100*(mortgage * rate / 100)/12)/100
  #  print (mortgage, monthly)
   # mortgage = mortgage - repay


def polyFunct(x):
    while (x >= 1 and x < 100):
        print (x, math.pow(x, 3), math.pow(x, 3) / 2)
        print (x, math.pow(x, 3) +2)
        x=x+1

def f(t):
    return math.pow(x,3) - 5 * math.pow(x, 2) + 8

def factorial(x):
    if (x <=0):
        return 1
    return x * factorial(x-1)

def binCoeff(x, y):
    return (factorial(x)/(factorial(y)*factorial(x-y)))

def main():
    y = 2
    for x in range(10, 40):
        print(x, factorial(x), binCoeff(x,y))

if __name__ == "__main__":
    main()


#x1 = 1
#inputs = {1,1.2,1.3,1.4,1.5,1.6,1.75,2,2.25}

# inputs = {1.5,1.51,1.52,1.53,1.6}
# for x in inputs:
#     y = math.pow(x, 3) - 5 * math.pow(x, 2) + 8
#     print (x, y)

# t1 = np.arange(1.0, 3, 0.001)
# plt.figure(1)
# plt.subplot(212)
# for x in t1:
# #    y = math.pow(x, 3) - 5 * math.pow(x, 2) + 8
#     y = math.pow(8/(5-x), 0.5)
#     #if (math.fabs(y) < 0.01):
#     print (x, y)
#     #plt.plot(x, y)

# x=1
# y=1
# count = 0
# while y > 0.01 and count < 100:
#    x = y
#    y = math.sqrt((8/(5-x)))
#    print (y)
#    count = count+1

#plt.show()


#x1 = np.arange(0, 5.0, 0.001)


#plt.figure(1)
#plt.subplot(211)
#plt.subplot(212)
#plt.plot(x1, f(x1))
#plt.show()

#pi = math.pi
#e = math.e

#print(pi,e)

#print(math.sqrt(pi))

#print(math.pow(math.sqrt(pi),2))
#help(math)
#print(math.pow(math.sqrt(pi)),2)