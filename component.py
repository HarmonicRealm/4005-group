import numpy as np

class Component():

	name = ''
	inspectionTime = 0

	def __init__(self, name, i):
		self.name = name
		if self.name == 'c1':
			self.inspectionTime = np.loadtxt('./servinsp1.dat')[i]
		elif self.name == 'c2':
			self.inspectionTime = np.loadtxt('./servinsp22.dat')[i]
		else:
			self.inspectionTime = np.loadtxt('./servinsp23.dat')[i]

	def getInspectionTime(self):
		return self.inspectionTime
	
	def getName(self):
		return self.name