# Write a method to compute all permutations of a string

import random
import math

def printperm(prefix, s):
	if len(s) == 0:
		print prefix
	else:
		for c in s:
			modified = list(s)
			modified.remove(c)
			printperm(prefix + c, modified)
	# TIME = O(n!)

def countperm(s):
	if len(s) == 0:
		return 1
	else:
		count = 0
		for c in s:
			modified = list(s)
			modified.remove(c)
			count += countperm(modified)
		return count


n = 5
codes = random.sample(xrange(65, 91), n)
# python strings are immutable, we will use a list of chars instead
string = []
for c in codes:
	string.append(str(unichr(c)))
print string

printperm("", string)

print "n! = %s" % math.factorial(n)
print "countperm() = %s" % countperm(string)