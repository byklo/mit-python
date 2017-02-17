# Write a script which generates an array of all number pairs from a set
# which uniquely add to a specified sum.

import random

# [ 3 5 1 4 2 ]
# x = 6
# expect: [ 51, 42 ]

def all_pairs(a, x):
	# return array of tuples that add up to x
	pairs = []
	dp = {}
	for val in a:
		if dp.has_key(x - val):
			pairs.append( (x-val, val) )
		dp[val] = True
	return pairs

a = random.sample(xrange(10), 5)
x = random.randint(5, 15)

print a
print x

print all_pairs(a, x)