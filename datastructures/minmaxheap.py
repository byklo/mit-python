import random
import heapq

# will implement min-max heaps using a min and a max heap
# the heaps are normal heaps but the important part is that they need
# to have a remove(item) method. the implemented remove(item) method
# runs in O(lg n) time so O(lg n) time overall is preserved for
# all heap operations.

def swap(array, a, b):
	temp = array[a]
	array[a] = array[b]
	array[b] = temp

def get_left(i):
	return (i + 1) * 2 - 1

def get_right(i):
	return (i + 1) * 2

def get_parent(i):
	return (i - 1) / 2

class min_heap(object):
	def __init__(self):
		self.heap = []
		self.item_index = {}

	def get_min(self):
		return self.heap[0] if len(self.heap) > 0 else None

	def delete_min(self):
		if len(self.heap) < 1:
			return None
		i = len(self.heap) - 1
		item = self.heap[0]
		swap(self.heap, 0, i)
		self.item_index[self.heap[0]] = 0
		self.heap.remove(item)
		del self.item_index[item]
		self.bubble_down(0)
		return item

	def insert(self, item):
		i = len(self.heap)
		self.heap.append(item)
		self.item_index[item] = i
		self.bubble_up(i)

	def remove(self, item):
		i = self.item_index[item]
		last = len(self.heap) - 1
		swap(self.heap, i, last)
		self.item_index[self.heap[i]] = i
		self.heap.remove(item)
		del self.item_index[item]
		self.bubble_down(i)

	def bubble_up(self, i):
		while i != 0 and self.heap[i] < self.heap[get_parent(i)]:
			self.item_index[self.heap[i]] = get_parent(i)
			self.item_index[self.heap[get_parent(i)]] = i
			swap(self.heap, i, get_parent(i))
			i = get_parent(i)

	def bubble_down(self, i):
		while i < len(self.heap):
			lesser_index = False
			minimum = float("inf")
			if get_right(i) < len(self.heap) and self.heap[get_right(i)] < minimum:
				minimum = self.heap[get_right(i)]
				lesser_index = get_right(i)
			if get_left(i) < len(self.heap) and self.heap[get_left(i)] < minimum:
				minimum = self.heap[get_left(i)]
				lesser_index = get_left(i)
			if lesser_index and self.heap[lesser_index] < self.heap[i]:
				swap(self.heap, lesser_index, i)
				self.item_index[self.heap[i]] = i
				self.item_index[self.heap[lesser_index]] = lesser_index
				i = lesser_index
			else:
				break

	def __repr__(self):
		return str(self.heap)

class max_heap(object):
	def __init__(self):
		self.heap = []
		self.item_index = {}

	def get_max(self):
		return self.heap[0] if len(self.heap) > 0 else None

	def delete_max(self):
		if len(self.heap) < 1:
			return None
		i = len(self.heap) - 1
		item = self.heap[0]
		swap(self.heap, 0, i)
		self.item_index[self.heap[0]] = 0
		self.heap.remove(item)
		del self.item_index[item]
		self.bubble_down(0)
		return item

	def insert(self, item):
		i = len(self.heap)
		self.heap.append(item)
		self.item_index[item] = i
		self.bubble_up(i)

	def remove(self, item):
		i = self.item_index[item]
		last = len(self.heap) - 1
		swap(self.heap, i, last)
		self.item_index[self.heap[i]] = i
		self.heap.remove(item)
		del self.item_index[item]
		self.bubble_down(i)

	def bubble_up(self, i):
		while i != 0 and self.heap[i] > self.heap[get_parent(i)]:
			self.item_index[self.heap[i]] = get_parent(i)
			self.item_index[self.heap[get_parent(i)]] = i
			swap(self.heap, i, get_parent(i))
			i = get_parent(i)

	def bubble_down(self, i):
		while i < len(self.heap):
			greater_index = False
			maximum = float("-inf")
			if get_right(i) < len(self.heap) and self.heap[get_right(i)] > maximum:
				maximum = self.heap[get_right(i)]
				greater_index = get_right(i)
			if get_left(i) < len(self.heap) and self.heap[get_left(i)] > maximum:
				maximum = self.heap[get_left(i)]
				greater_index = get_left(i)
			if greater_index and self.heap[greater_index] > self.heap[i]:
				swap(self.heap, greater_index, i)
				self.item_index[self.heap[i]] = i
				self.item_index[self.heap[greater_index]] = greater_index
				i = greater_index
			else:
				break

	def __repr__(self):
		return str(self.heap)

class min_max_heap(object):
	def __init__(self):
		self.minheap = min_heap()
		self.maxheap = max_heap()

	def insert(self, item):
		self.minheap.insert(item)
		self.maxheap.insert(item)

	def get_min(self):
		return self.minheap.get_min()

	def get_max(self):
		return self.maxheap.get_max()

	def delete_min(self):
		min_item = self.minheap.delete_min()
		if min_item is not None:
			self.maxheap.remove(min_item)
		return min_item

	def delete_max(self):
		max_item = self.maxheap.delete_max()
		if max_item is not None:
			self.minheap.remove(max_item)
		return max_item


# a = random.sample(xrange(20), 10)
a = [ 5, 1, 3, 8, 9, 6, 4, 2]
print a
print sorted(a)

# b = list(a)
# heapq.heapify(b)

# minh = min_heap()
# maxh = max_heap()
# for x in a:
# 	minh.insert(x)
# 	maxh.insert(x)

# for x in a:
# 	print "%s %s" % (minh.delete_min(), maxh.delete_max())

mmh = min_max_heap()
for x in a:
	mmh.insert(x)

for i in xrange(len(a)/2):
	print mmh.delete_min()
	print mmh.delete_max()




