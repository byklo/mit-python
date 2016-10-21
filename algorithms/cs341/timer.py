import time

class Timer:
	def __init__(self):
		self.start_time = 0
		self.end_time = 0
		self.label = ""

	def start(self, _label):
		self.start_time = time.time()
		self.label = _label

	def end(self):
		self.end_time = time.time()
		print "[TIME - %s] %.4f" % (self.label, self.end_time - self.start_time)