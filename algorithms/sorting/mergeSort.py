#!/usr/bin/python

import sys

def merge(a1, a2):
	i1, i2 = 0, 0
	a3 = []
	while not (len(a1) == 0 and len(a2) == 0):
		if len(a2) == 0:
			a3.append(a1[0])
			del a1[0]
		elif len(a1) == 0:
			a3.append(a2[0])
			del a2[0]
		elif a1[0] <= a2[0]:
			a3.append(a1[0])
			del a1[0]
		else:
			a3.append(a2[0])
			del a2[0]
	return a3

def mergeSort(a):
	if len(a) == 1:
		return a
	else:
		k = len(a) / 2
		merged = merge(mergeSort(a[:k]), mergeSort(a[k:]))
		return merged

verbose = sys.argv[1].lower() == "true"
a = [ int(x) for x in sys.argv[2:] ]
print "Unsorted ->", a
sortedA = mergeSort(a)
print "Sorted ->", sortedA
