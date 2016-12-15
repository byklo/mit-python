# A magic index in an array A[1 .. n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

import random

def magic_linear(a):
	# O(n) iterate through the elements checking A[i] = i
	for (i, x) in enumerate(a):
		if a[i] == i + 1:
			return i + 1
	return -1
	# TIME = O(n)

def magic_log(a, l, r):
	# idea: can implement binary-like search because we can compare index i to a[i]
	if l > r:
		return -1
	index = (l + r) / 2
	if a[index] == index + 1:
		return index + 1
	elif a[index] < index + 1:
		# element is less than index, recurse right
		return magic_log(a, index+1, r)
	else:
		return magic_log(a, l, index-1)
	# TIME
	#	recurse on half problem size
	#	T(n) = 2*T(n/2) + c
	#	T(n) = O(lg n)

# 1 2 3 4 [5] 6 7 8
# 0 1 2 3 [5] 7 8 9

a = random.sample(xrange(0, 20), 10)
a = sorted(a)

print a
print magic_linear(a)
print magic_log(a, 0, len(a) - 1)