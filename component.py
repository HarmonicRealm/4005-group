from constants import *
import numpy as np
import threading

shm_component_1 = threading.Lock()
component1 = np.loadtxt('./dat/servinsp1.dat').tolist()
component2 = np.loadtxt('./dat/servinsp22.dat')
component3 = np.loadtxt('./dat/servinsp23.dat')

class component():
	def __init__(self, name, i):
		self.name = name
		if self.name == COMPONENT1:
			global shm_component_1
			shm_component_1.acquire()
			self.inspectionTime = component1.pop()
			shm_component_1.release()
		elif self.name == COMPONENT2:
			self.inspectionTime = component2[i]
		else:
			self.inspectionTime = component3[i]

	def getInspectionTime(self):
		return self.inspectionTime
	
	def getName(self):
		return self.name