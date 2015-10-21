#!/usr/bin/python

import sys
import time

def fibRecursive(k):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	else:
		return fibRecursive(k-1) + fibRecursive(k-2)

def fibIterative(k):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	else:
		term1, term2 = 1, 1
		i = 2
		while (i < k):
			term1 += term2
			temp = term1
			term1 = term2
			term2 = temp
			i += 1
		return term2

def fibDynamic(k, helper):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	elif helper.has_key(k):
		return helper.get(k)
	else:
		value = fibDynamic(k-1, helper) + fibDynamic(k-2, helper)
		helper[k] = value
		return value

fibdic = {}

k = int(sys.argv[1])

#timeRecursive = time.time()
#fibRecursive(k)
#timeRecursive = time.time() - timeRecursive

timeIterative = time.time()
fibIterative(k)
timeIterative = time.time() - timeIterative

timeDynamic = time.time()
fibDynamic(k, fibdic)
timeDynamic = time.time() - timeDynamic

#print "Recursive\t=\t%s" % timeRecursive
print "Iterative\t=\t%s" % timeIterative
print "Dynamic\t\t=\t%s" % timeDynamic
