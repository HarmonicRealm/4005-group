import time
import threading

class workstation(threading.Thread):
	def __init__(self, name, shm):
		threading.Thread.__init__(self)
		self.name = name
		self.shared_mem = shm

	def run(self):
		while 1:
			return