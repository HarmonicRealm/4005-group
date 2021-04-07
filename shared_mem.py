import threading

class shared_mem():
	def __init__(self):
		self.max_buff_size = 2
		self.buff_ws1c1 = 0
		self.buff_ws2c1 = 0
		self.buff_ws2c2 = 0
		self.buff_ws3c1 = 0
		self.buff_ws3c3 = 0

		self.lock_ws1c1 = threading.Lock()
		self.lock_ws2c1 = threading.Lock()
		self.lock_ws2c2 = threading.Lock()
		self.lock_ws3c1 = threading.Lock()
		self.lock_ws3c3 = threading.Lock()

	def write_buff(self, workstation, component):

## 		Workstation 1 component 1 buffer

		if workstation == WORKSTATION1:
			if component == COMPONENT1:
				self.lock_ws1c1.acquire()
				self.buff_ws1c1 += 1
				self.lock_ws1c1.release()
				return

##		Workstation 2 component 1 & 2 buffer

		if workstation == WORKSTATION2:
			if component == COMPONENT1:
				self.lock_ws2c1.acquire()
				self.buff_ws2c1 += 1
				self.lock_ws2c1.release()
				return

			if component == COMPONENT2:
				self.lock_ws2c2.acquire()
				self.buff_ws2c2 += 1
				self.lock_ws2c2.release()
				return

##		Workstation 3 component 1 & 3 buffer

		if workstation == WORKSTATION3:
			if component == COMPONENT1:
				self.lock_ws3c1.acquire()
				self.buff_ws3c1 += 1
				self.lock_ws3c1.release()
				return

			if component == COMPONENT3:
				self.lock_ws3c3.acquire()
				self.buff_ws3c3 += 1
				self.lock_ws3c3.release()
				return

		return

	def read_buff(self, workstation, component):
		x = -1

		if workstation == WORKSTATION1:
			if component == COMPONENT1:
				self.lock_ws1c1.acquire()
				x = self.buff_ws1c1
				self.lock_ws1c1.release()

##		Workstation 2 component 1 & 2 buffer

		if workstation == WORKSTATION2:
			if component == COMPONENT1:
				self.lock_ws2c1.acquire()
				x = self.buff_ws2c1
				self.lock_ws2c1.release()

			if component == COMPONENT2:
				self.lock_ws2c2.acquire()
				x = self.buff_ws2c2
				self.lock_ws2c2.release()

##		Workstation 3 component 1 & 3 buffer

		if workstation == WORKSTATION3:
			if component == COMPONENT1:
				self.lock_ws3c1.acquire()
				x = self.buff_ws3c1
				self.lock_ws3c1.release()

			if component == COMPONENT3:
				self.lock_ws3c3.acquire()
				x = self.buff_ws3c3
				self.lock_ws3c3.release()

		return x