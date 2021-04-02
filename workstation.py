import threading
from component import Component
import threading
import time

exitFlag = 0

class Workstation(threading.Thread):

	def __init__(self, name, accept, builds):
		self.name = name
		self.status = 'IDLE'
		self.accept = accept
		self.builds = builds
		self.productsBuilt = 0

		if self.name == 'ws1':
			self.arr = [0,0]
		else:
			self.arr = [0,0,0,0]

	def storeComponent(self, component):
		for i in range(len(self.arr)):
			if self.arr[i] == 0:
				self.arr[i] = component.getName()
				print('stored {} in {} buff'.format(component.getName(), self.name))
				break
		self.checkComponent()
		return

	def checkComponent(self):
		if self.name == 'ws1' and self.arr.count('c1') == 2:
			self.arr.remove('c1')
			self.arr.remove('c1')
			self.arr.append(0)
			self.arr.append(0)
			self.buildProduct()

		elif self.name == 'ws2' and 'c1' in self.arr and 'c2' in self.arr:
			self.arr.remove('c1')
			self.arr.remove('c2')
			self.arr.append(0)
			self.arr.append(0)
			self.buildProduct()


		elif self.name == 'ws3' and 'c1' in self.arr and 'c3' in self.arr:
			self.arr.remove('c1')
			self.arr.remove('c3')
			self.arr.append(0)
			self.arr.append(0)
			self.buildProduct()

		return

	def buildProduct(self):
		print('building product {}'.format(self.builds))
		self.productsBuilt+=1
		return

	def checkCapacity(self, component):
		if component.getName() in self.accept:
			count = self.arr.count(component.getName())
		else:
			count = 999
		return count

	def getBuff(self):
		return self.arr

	def getProductsBuilt(self):
		return self.productsBuilt

	def accepts(self):
		return self.accept