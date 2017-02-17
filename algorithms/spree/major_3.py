# Given an integer array of size n, find all elements that appear
# more than floor(n/3) times. The algorithm should run in
# linear time and in O(1) space.

import random

# crappy solution, monte carlo randomized
# there should be a deterministic way of doing this
# mm, counting in sets of threes, eliminating matches or something
def major(a):
	n = len(a)
	target = (n/3) + 1
	while True:
		items = [ random.choice(a) for x in xrange(4) ]
		for x in items:
			count = 0
			for y in a:
				if y == x:
					count += 1
					if count >= target:
						return x
	return False

n = random.randint(10, 12)
n = 1000000
a = [7] * ((n/3) + 1)
a += random.sample(xrange(n), n - ((n/3) + 1))

# print a
print major(a)