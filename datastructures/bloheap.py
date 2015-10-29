class Heap:
	'''
	This is a heap class definition
	'''

	def __init__(self, a):
		self.array = [ None ]
		self.array.extend(list(a))
		for i in xrange((len(a) / 2), 0, -1):
			self.maxHeapify(i)

	def __str__(self):
		return self.array[1:].__str__()

	def insert(self, newEntry):
		if isinstance(newEntry, int):
			self.array.append(newEntry)
			self.percUp(len(self.array) - 1)
		else:
			print "ERROR: Not int. Could not insert entry ->", newEntry

	def checkMax(self):
		return self.array[1]
	
	def popMax(self):
		max = 0 + self.array[1]
		self.swap(1, len(self.array) - 1)
		del self.array[len(self.array) - 1]
		self.maxHeapify(1)
		return max

	def sort(self):
		s = list(self.array)
		maxIndex = len(s) - 1
		while maxIndex > 1:
			self.swap(1, maxIndex, s)
			maxIndex -= 1
			self.maxHeapify(1, maxIndex=maxIndex, a=s)
		print s[1:]
	
	def maxHeapify(self, i, maxIndex=None, a=None):
		array = a if a else self.array
		if not maxIndex:
			maxIndex = len(array) - 1
		l, r = self.left(i), self.right(i)
		largest = i
		if l <= maxIndex and array[i] < array[l]:
			largest = l
		if r <= maxIndex and array[largest] < array[r]:
			largest = r
		if largest != i:
			self.swap(i, largest, array)
			self.maxHeapify(largest, maxIndex, array)

	def percUp(self, i):	
		a = self.array
		p = self.parent(i)
		while p > 0:
			if a[p] < a[i]:
				self.swap(i, p)
				i = p
				p = self.parent(p)
			else:
				break
	
	def isHeap(self):
		a = self.array
		maxIndex = len(a) - 1
		for i in xrange((len(a) / 2), 0, -1):
			l, r = self.left(i), self.right(i)
			if l <= maxIndex and a[i] < a[l]:
				return False
			if r <= maxIndex and a[i] < a[r]:
				return False
		return True

	def swap(self, i, j, a=None):
		array = a if a else self.array
		temp = array[i]
		array[i] = array[j]
		array[j] = temp
		return

	def left(self, i):
		return i * 2

	def right(self, i):
		return i * 2 + 1
	
	def parent(self, i):
		return i / 2