# sum of previous smaller numbers
# [ 2, 5, 1, 9, 3 ]
# [ 0, 2, 0, 8, 3 ]

import random

def sps_quad(v):
	# quadratic
	n = len(v)
	retv = [ 0 for x in xrange(n) ]
	for i,x in enumerate(v):
		for j in xrange(i, n):
			retv[j] += v[i] if v[j] > v[i] else 0
	return retv

def sps(v):
	return

v = random.sample(xrange(9), 5)
v = [ 2, 5, 1, 9, 3 ]

print v
print sps_quad(v)