class Component():

	name = ''
	inspectionTime = 0

	def __init__(self, name):
		self.name = name
		self.inspectionTime = 0

	def getInspectionTime(self):
		return self.inspectionTime
	
	def getName(self):
		return self.name