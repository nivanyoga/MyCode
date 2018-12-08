__author__ = 'DEFAULT'
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()




# ax = plt.subplot(111)
#
# t = np.arange(0.0, 5.0, 0.001)
# #s = np.cos(2*np.pi*t)
# s = np.sin(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)
#
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='red', shrink=0.05),
#             )
#
# plt.ylim(-2,2)
# plt.show()
#
#
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='y', alpha=0.75)
#
#
# plt.xlabel('Farts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# #plt.grid(True)
# plt.grid(False)
# plt.show()