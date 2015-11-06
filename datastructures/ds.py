from bloheap import *
from bst import *
import random

# INIT
#a = random.sample(xrange(0, 50), 20)
a = random.sample(xrange(0, 50), 10)

# HEAP
# h = Heap(a)
# 
# print h
# print h.isHeap()
# 
# h.insert(75)
# 
# print h
# print h.checkMax()
# 
# print "just popped", h.popMax()
#
# print h
# print h.isHeap()
# 
# h.sort()

# BST
tree = BST()
for i in a:
	tree.insert(i)

tree.info()

print tree.nodesLessThan(20)