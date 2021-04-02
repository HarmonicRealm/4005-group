import sys
import time as t
import numpy as np
from datetime import datetime

from component import *
from inspector import *
from product import *
from workstation import *

try:
	ws1 = Workstation('ws1', 'c1',  'p1')
	ws2 = Workstation('ws2', 'c1c2','p2')
	ws3 = Workstation('ws3', 'c1c3','p3')

	i1 = Inspector('i1')
	i2 = Inspector('i2')

	ws1.start()
	ws2.start()
	ws3.start()
	i1.start()
	i2.start()

except KeyboardInterrupt:
	sys.exit()


'''
capacity = [
	ws1.checkCapacity(i),
	ws2.checkCapacity(i),
	ws3.checkCapacity(i),
]

if min(range(len(capacity)), key=capacity.__getitem__) == 0 and i.getName() in ws1.accepts() and ws1.getBuff().count(i.getName()) <= 1:
	ws1.storeComponent(i)
elif min(range(len(capacity)), key=capacity.__getitem__) == 1 and i.getName() in ws2.accepts() and ws2.getBuff().count(i.getName()) <= 1:
	ws2.storeComponent(i)
elif min(range(len(capacity)), key=capacity.__getitem__) == 2 and i.getName() in ws3.accepts() and ws3.getBuff().count(i.getName()) <= 1:
	ws3.storeComponent(i)
elif i.getName() in ws1.accepts() and ws1.getBuff().count(i.getName()) <= 1:
	ws1.storeComponent(i)
elif i.getName() in ws2.accepts() and ws2.getBuff().count(i.getName()) <= 1:
	ws2.storeComponent(i)
elif i.getName() in ws3.accepts() and ws3.getBuff().count(i.getName()) <= 1:
	ws3.storeComponent(i)


print('products built:\nws1: {}\nws2: {}\nws3: {}'.format(ws1.getProductsBuilt(), ws2.getProductsBuilt(), ws3.getProductsBuilt()))
'''