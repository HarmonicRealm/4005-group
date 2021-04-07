from constants import *
import numpy as np

class component():
	def __init__(self, name, i):
		self.name = name
		if self.name == COMPONENT1:
			self.inspectionTime = np.loadtxt('./dat/servinsp1.dat')[i]
		elif self.name == COMPONENT2:
			self.inspectionTime = np.loadtxt('./dat/servinsp22.dat')[i]
		else:
			self.inspectionTime = np.loadtxt('./dat/servinsp23.dat')[i]

	def getInspectionTime(self):
		return self.inspectionTime
	
	def getName(self):
		return self.name