import time
import random
import threading
from constants import *
from component import component

class inspector(threading.Thread):
	def __init__(self, name, shm):
		threading.Thread.__init__(self)
		self.name = name
		self.status = START
		self.component = None
		self.shared_mem = shm

##	inspector sets components, inspects, then releases

	def run(self):
		for i in range(300):
			self.setComponent(i)
			self.inspectComponent()
			self.releaseComponent()
		return

## inspector gets C1 if its inspector 1, C2 or C3 if its inspector 2
	
	def setComponent(self, i):
		if self.getName() == INSPECTOR1:
			self.component = component(COMPONENT1, i)
		else:
			if random.randint(2,3) == 2:
				self.component = component(COMPONENT2, i)
			else:
				self.component = component(COMPONENT3, i)

		#print("{} got {}".format(self.getName(), self.component.getName()))
		return

## inspector waits the component time

	def inspectComponent(self):
		t = self.getComponent().getInspectionTime()
		time.sleep(t)

		#print ("{} waited {}".format(self.getName(), t))
		return

## inspector sends the component to the shared memory

	def releaseComponent(self):
		if self.getName() == INSPECTOR1:
			
		else:

		#print("{} sent {} to {}".format(self.getName(), self.component.getName(), WORKSTATION1))
		self.removeComponent()
		return

## attribute getters
	
	def getName(self):
		return self.name

	def getStatus(self):
		return self.status

	def getComponent(self):
		return self.component

	def removeComponent(self):
		self.component = None
		return
