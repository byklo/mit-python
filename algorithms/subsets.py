# Print all the subsets of a given set

import random

def subsets(remaining, pre):
	if len(remaining) < 1:
		# no more remaining elements to branch
		print pre
	else:
		# pick a remaining element and branch (1) with and (2) without it
		element = remaining.pop()
		# have to use list() to facilitate copies
		# python naturally passes a reference
		subsets(list(remaining), pre + [element])
		subsets(list(remaining), pre)

s = random.sample(xrange(20), 5)
s = sorted(s)

subsets(s, [])
