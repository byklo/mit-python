#!/usr/bin/python

import sys
import random

# buildMaxHeap
def buildMaxHeap(a):
	out = list(a)
	for i in xrange((len(out) - 1)/2, 0, -1):
		maxHeapify(out, i)
	return out

# maxHeapify
#	assumes left(i) and right(i) are CORRECT max heaps
#	the violation is assumed to be at i
def maxHeapify(a, i, maxIndex=None):
	if not maxIndex:
		maxIndex = len(a) - 1
	l = left(i)
	r = right(i)
	largest = i
	if l <= maxIndex and a[l] > a[i]:
		largest = l
	if r <= maxIndex and a[r] > a[largest]:
		largest = r
	if largest != i:
		temp = a[i]
		a[i] = a[largest]
		a[largest] = temp
		maxHeapify(a, largest, maxIndex)
	else:
		# no violation at a[i]
		# OR
		# reached leaf
		return

def isHeap(a):
	n = len(a) - 1
	for i in xrange(n/2, 0, -1):
		l = left(i)
		r = right(i)
		if l <= n and a[l] > a[i]:
			return False
		if r <= n and a[r] > a[i]:
			return False
	return True

def left(i):
	return i * 2

def right(i):
	return i * 2 + 1

# heapSort
def heapSort(a):
	heap = buildMaxHeap(a)
	lastIndex = len(heap) - 1
	while lastIndex > 1:
		swap(heap, 1, lastIndex)
		lastIndex -= 1
		maxHeapify(heap, 1, lastIndex)
	return heap

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

# to satisfy the heap indices, assign None to a[0], heap starts at a[1]
a = [ None ]
a.extend(random.sample(xrange(0, 20), 11))
print a

heapd = buildMaxHeap(a)
print heapd, "is a heap" if isHeap(heapd) else "is not a heap"

sortd = heapSort(a)
print sortd
