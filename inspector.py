import random
from component import Component
import threading
import time

exitFlag = 0


class Inspector(threading.Thread):

	def __init__(self, name):
		self.name = name
		self.status = 'WORK'
		self.component = None

	def run(self):
		if self.status = 'WORK':
			for i in range(300):
				self.component = getComponent(i)
				self.inpectComponent()
				self.releaseComponent()

	def getComponent(self, i):
		if self.name == 'i1':
			self.component = Component('c1', i)
		if self.name == 'i2':
			if random.randint(2,3) == 2:
				self.component = Component('c2', i)
			else:
				self.component = Component('c3', i)
		return self.component

	def inspectComponent(self):
		time.sleep(self.component.getInspectionTime())
		return

	def releaseComponent(self):
		return
