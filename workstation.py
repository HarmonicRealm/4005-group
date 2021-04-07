import time
import numpy as np
import threading
from constants import *


class workstation(threading.Thread):
	def __init__(self, name, shm):
		threading.Thread.__init__(self)
		self.name = name
		self.products_made = 0
		self.shared_mem = shm
		self.production_time = 0
		self.total_work_time = 0

	def run(self):
		while self.shared_mem.isRunning():
			if self.searchBuffer(): 
				self.setProductionTime()
				self.setProductsMade()

		self.dumpStats()
		return


## search the buffer for components

	def searchBuffer(self):
		if self.getName() == WORKSTATION1:
			if self.shared_mem.read(WORKSTATION1, COMPONENT1) > 0:
				self.shared_mem.remove(WORKSTATION1, COMPONENT1)
				return True

		elif self.getName() == WORKSTATION2:
			if  self.shared_mem.read(WORKSTATION2, COMPONENT1) > 0 and \
				self.shared_mem.read(WORKSTATION2, COMPONENT2) > 0:
				self.shared_mem.remove(WORKSTATION1, COMPONENT1)
				self.shared_mem.remove(WORKSTATION2, COMPONENT2)
				return True

		elif self.getName() == WORKSTATION3:
			if  self.shared_mem.read(WORKSTATION3, COMPONENT1) > 0 and \
				self.shared_mem.read(WORKSTATION3, COMPONENT3) > 0:
				self.shared_mem.remove(WORKSTATION1, COMPONENT1)
				self.shared_mem.remove(WORKSTATION3, COMPONENT3)
				return True

		return False


## get production time from dat file

	def setProductionTime(self):
		if self.getName() == WORKSTATION1:
			self.production_time = np.loadtxt('./dat/ws1.dat')[self.getProductsMade()]
		elif self.getName() == WORKSTATION2:
			self.production_time = np.loadtxt('./dat/ws2.dat')[self.getProductsMade()]
		else:
			self.production_time = np.loadtxt('./dat/ws3.dat')[self.getProductsMade()]
		time.sleep(self.production_time)
		print('{} waited {}'.format(self.getName(), self.production_time))

##	dump stats into txt files

	def dumpStats(self):
		t = 0
		if self.getName() == WORKSTATION1:
			f = './output/ws1out'
		elif self.getName() == WORKSTATION2:
			f = './output/ws2out'
		else:
			f = './output/ws3out'
		with open(f, 'w') as file:
			file.write('{}\ntime: {}\nproducts made: {}'.format(self.getName(), t, self.getProductsMade()))


## getters and setters

	def getName(self):
		return self.name

	def getProductsMade(self):
		return self.products_made

	def setProductsMade(self):
		self.products_made += 1
		print("{} made a product".format(self.getName()))

	def getTotalWorkTime(self):
		return self.total_work_time

