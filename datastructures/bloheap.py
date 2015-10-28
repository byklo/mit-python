# interface
# constructor Heap(list<int>)
# sortedList sort()
# void insert(int)
# list = [ 3, 5, 5, 7, 1, 4, 8, 9, 2 ]
# heap = Heap(list)
# sortedList = heap.sort()
# heap.insert(28)
# heap.checkMax()
# heap.popMax()

import random

class Heap:
	'''
	This is a heap class definition
	'''

	def __init__(self, a):
		self.array = [None]
		self.array.extend(list(a))
		for i in xrange((len(a) / 2), 0, -1):
			self.maxHeapify(i)

	def insert(self, newEntry):
		self.array.append(newEntry)
		self.percUp(len(self.array) - 1)

	def checkMax(self):
		return self.array[1]
	
	def popMax(self):
		max = 0 + self.array[1]
		self.swap(1, len(self.array) - 1)
		del self.array[len(self.array) - 1]
		self.maxHeapify(1)

	def sort(self):
		pass
	
	def prnt(self):
		print self.array[1:]
	
	def maxHeapify(self, i, maxIndex=None):
		a = self.array
		if not maxIndex:
			maxIndex = len(a) - 1
		l, r = self.left(i), self.right(i)
		largest = i
		if l <= maxIndex and a[i] < a[l]:
			largest = l
		if r <= maxIndex and a[largest] < a[r]:
			largest = r
		if largest != i:
			self.swap(i, largest)
			self.maxHeapify(largest, maxIndex)
		else:
			return

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

	def swap(self, i, j):
		temp = self.array[i]
		self.array[i] = self.array[j]
		self.array[j] = temp
		return

	def left(self, i):
		return i * 2

	def right(self, i):
		return i * 2 + 1
	
	def parent(self, i):
		return i / 2

a = random.sample(xrange(0, 30), 8)
heap = Heap(a)
heap.prnt()
print "is heap?", heap.isHeap()
heap.insert(40)
heap.prnt()
