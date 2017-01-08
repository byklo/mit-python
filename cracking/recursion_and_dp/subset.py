# Write a method to return all subsets of a set

import random

def subsets_print(p, s):
	if len(s) == 0:
		print p
	else:
		element = s.pop()
		subsets_print(list(p), list(s))
		subsets_print(list(p + [element]), list(s))
	# TIME = O(2^n)

def subsets_return(p, s, ret):
	if len(s) == 0:
		ret.append(p)
	else:
		element = s.pop()
		subsets_return(list(p), list(s), ret)
		subsets_return(list(p + [element]), list(s), ret)

def subsets_dp(s):
	# if |s| = n, there will be 2^n subsets
	# we can dp our way up from smallets subsets which we know trivially
	# we can make a list of list of subsets in increasing size
	# subsets[k] = list of subsets of size k
	# not possible, will be iterating through lists of size k-1 subsets to make size k subsets which is O(2^n)
	# there is no polynomial time algorithm to generate 2^n objects
	pass


n = 5
s = random.sample(xrange(10), n)
print s
# subsets_print([], s)
ret = []
subsets_return([], s, ret)
print ret

print 2**n
print len(ret)