#!/usr/bin/python

import sys

def bubbleSort(a, verbose):
	unsortedLength = len(a)
	while unsortedLength > 0:
		for i in xrange(unsortedLength):
			if i != unsortedLength - 1 and a[i] > a[i+1]:
				print "// swapping %s with %s" % (a[i], a[i+1])
				temp = a[i]
				a[i] = a[i+1]
				a[i+1] = temp
				if verbose:
					print a
		unsortedLength -= 1
	return a

verbose = sys.argv[1].lower() == "true"
sortThis = [ int(x) for x in sys.argv[2:] ]

print "Unsorted ->\t", sortThis
print "Sorted ->\t", bubbleSort(sortThis, verbose)
