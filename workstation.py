import time
import threading
from constants import *

class workstation(threading.Thread):
	def __init__(self, name, shm):
		threading.Thread.__init__(self)
		self.name = name
		self.products_made = 0
		self.shared_mem = shm

	def run(self):
		while self.shared_mem.isRunning():
			if self.getName() == WORKSTATION1:
				if self.shared_mem.read(WORKSTATION1, COMPONENT1) > 0:
					time.sleep(5)
					self.shared_mem.remove(WORKSTATION1, COMPONENT1)
					self.setProductsMade()
					print("{} made a product".format(self.getName()))

			elif self.getName() == WORKSTATION2:
				if  self.shared_mem.read(WORKSTATION2, COMPONENT1) > 0 and \
					self.shared_mem.read(WORKSTATION2, COMPONENT2) > 0:
					time.sleep(5)
					self.shared_mem.remove(WORKSTATION1, COMPONENT1)
					self.shared_mem.remove(WORKSTATION2, COMPONENT2)
					self.setProductsMade()
					print("{} made a product".format(self.getName()))

			elif self.getName() == WORKSTATION3:
				if  self.shared_mem.read(WORKSTATION3, COMPONENT1) > 0 and \
					self.shared_mem.read(WORKSTATION3, COMPONENT3) > 0:
					time.sleep(5)
					self.shared_mem.remove(WORKSTATION1, COMPONENT1)
					self.shared_mem.remove(WORKSTATION3, COMPONENT3)
					self.setProductsMade()
					print("{} made a product".format(self.getName()))

		self.dumpStats()
		return


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
			file.write('{} time: {}'.format(self.getName(), t))


## getters and setters

	def getName(self):
		return self.name

	def getProductsMade(self):
		return self.products_made

	def setProductsMade(self):
		self.products_made += 1

	def dumpStats(self):
		return
