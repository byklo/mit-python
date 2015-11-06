#!/usr/bin/python

import sys
import random

def radixSort(a):
	BASE = 10
	place = 1
	nextDigitExists = True

	while nextDigitExists:
		nextDigitExists = False
		buckets = [[] for x in xrange(BASE)]

		for x in a:
			if x >= place:
				digit = (x / place) % BASE
				buckets[digit].append(x)
				if (not nextDigitExists) and x >= place * BASE:
					nextDigitExists = True
			else:
				buckets[0].append(x)

		a[:] = []

		for i in xrange(BASE):
			for j in buckets[i]:
				a.append(j)

		place *= BASE

a = random.sample(xrange(50), 20)
print "Unsorted =\t", a

radixSort(a)
print "Sorted =\t", a
