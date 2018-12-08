__author__ = 'DEFAULT'
import numpy as np
import matplotlib.pyplot as plt

with plt.style.context(('dark_background')):
    #plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
    plt.plot(np.cos(np.linspace(0, 2 * np.pi)), 'b-o')
    plt.plot(np.tan(np.linspace(0, 2 * np.pi)), 'y-o')
plt.show()

# t = np.arange(0.0, 2.0, 0.01)
# s = np.sin(2*np.pi*t)
#
# plt.plot(t,s)
# plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
# plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
# plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{cos}(2 \theta t)$',
#          fontsize=20)
# plt.xlabel('time (s)')
# plt.ylabel('volts (mV)')
# plt.show()