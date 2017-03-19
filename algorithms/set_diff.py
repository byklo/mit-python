# set difference
# given A = [ 1 2 3 4 ], B = [ 3 4 5 6 ], return D = [ 1 2 5 6 ]

import random

def set_diff(a, b):
	duplicates = {}
	uniques = {}
	combined = a + b
	for x in combined:
		if x in uniques:
			duplicates[x] = 1
		else:
			uniques[x] = 1
	output = []
	for x in combined:
		if x not in duplicates:
			output.append(x)
	return output

a = sorted(random.sample(xrange(10), 5))
b = sorted(random.sample(xrange(10), 5))

print "A : %s" % a
print "B : %s" % b
print "diff : %s" % set_diff(a, b)