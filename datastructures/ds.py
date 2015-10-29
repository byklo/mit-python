from bloheap import Heap
import random

a = random.sample(xrange(0, 50), 20)
h = Heap(a)

print h
print h.isHeap()

h.insert(75)

print h

print h.checkMax()

print "just popped", h.popMax()

print h
print h.isHeap()

h.sort()