# least sum terms in square

# given 81, return 1 (9^2)
# given 5, return 2 (2^2 + 1^2)

import random
import math

def least_sums(x):
	if x == 1:
		return 1
	if x == 0:
		return 0
	else:
		partial = math.floor(math.sqrt(x))
		remainder = x - partial**2
		return 1 + least_sums(remainder)

x = random.randint(0, 120)
print "%s -> %s" % (x, least_sums(x))