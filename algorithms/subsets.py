# Print all the subsets of a given set

import random

def subsets(s, pre):
	if len(s) < 1:
		print pre
	else:
		element = s.pop()
		subsets(list(s), pre + [element])
		subsets(list(s), pre)

s = random.sample(xrange(20), 5)
s = sorted(s)

subsets(s, [])
