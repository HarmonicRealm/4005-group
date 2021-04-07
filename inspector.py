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
		self.components_inspected = 0
		self.total_work_time = 0
		self.total_blocked_time = 0

##	inspector sets components, inspects, then releases

	def run(self):
		while self.getComponentsInspected() <= SIZE and self.shared_mem.isRunning():
			self.setComponent(self.getComponentsInspected())
			self.inspectComponent()
			while self.Blocked() and self.shared_mem.isRunning(): 1
			self.releaseComponent()

		self.shared_mem.quit()
		self.dumpStats()
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

		print("{} got {}".format(self.getName(), self.component.getName()))
		return

## inspector waits the component time

	def inspectComponent(self):
		t = self.getComponent().getInspectionTime()
		time.sleep(t)

		print ("{} waited {}".format(self.getName(), t))
		self.components_inspected += 1
		return


## check to see if able to deposit the component in associated buffer

	def Blocked(self):
		x = False

		if self.getName() == INSPECTOR1:
			if  self.shared_mem.read(WORKSTATION1, COMPONENT1) == 2 and \
				self.shared_mem.read(WORKSTATION2, COMPONENT1) == 2 and \
				self.shared_mem.read(WORKSTATION3, COMPONENT1) == 2:
				x = True
		
		if self.component.getName() == COMPONENT2:
			if self.shared_mem.read(WORKSTATION2, COMPONENT2) == 2:
				x = True
		
		if self.component.getName() == COMPONENT3:
			if self.shared_mem.read(WORKSTATION3, COMPONENT3) == 2:
				x = True
		
		return x


## inspector sends the component to the shared memory

	def releaseComponent(self):
		WORKSTATIONX = -1

		if self.getName() == INSPECTOR1:
			WORKSTATIONX = self.shared_mem.leastComponent1()
			self.shared_mem.write(WORKSTATIONX, COMPONENT1)

		elif self.component.getName() == COMPONENT2:
			WORKSTATIONX = WORKSTATION2
			self.shared_mem.write(WORKSTATION2, COMPONENT2)
		
		else:
			WORKSTATIONX = WORKSTATION3
			self.shared_mem.write(WORKSTATION3, COMPONENT3)

		print("{} sent {} to {}".format(self.getName(), self.component.getName(), WORKSTATIONX))
		self.removeComponent()
		return


##	dump stats into txt files

	def dumpStats(self):
		t = 0
		if self.getName() == INSPECTOR1:
			f = './output/insp1out'
		else:
			f = './output/insp2out'
		with open(f, 'w') as file:
			file.write('{}\ntime: {}\ncomponents inspected:{}'.format(self.getName(), t, self.getComponentsInspected()))


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

	def getComponentsInspected(self):
		return self.components_inspected

	def getTotalWorkTime(self):
		return self.total_work_time

	def getTotalBlockedTime(self):
		return self.total_blocked_time
