import pylab
import numpy as np
import scipy.stats as stats

ws1 = np.loadtxt('./ws1.dat')
ws2 = np.loadtxt('./ws2.dat')
ws3 = np.loadtxt('./ws3.dat')
servinsp1  = np.loadtxt('./servinsp1.dat')
servinsp22 = np.loadtxt('./servinsp22.dat')
servinsp23 = np.loadtxt('./servinsp23.dat')

stats.probplot(ws1, plot=pylab)
pylab.show()