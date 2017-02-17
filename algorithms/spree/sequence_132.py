# Given a sequence of n integers a[1], a[2], ..., a[n], a 132 pattern is a subsequence a[i], a[j], a[k]
# such that i < j < k and a[i] < a[k] < a[j]. Design an algorithm that takes a list of n numbers as
# input and checks whether there is a 132 pattern in the list.
# 
# Note: n will be less than 15,000.
# 
# Example 1:
# Input: [1, 2, 3, 4]
# 
# Output: False
# 
# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]
# 
# Output: True
# 
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]
# 
# Output: True
# 
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

import random

# O(n^2) solution
def seq_slow(a):
	table = {}
	for x in a:
		if not table.has_key(x):
			table[x] = x
		for k,v in table.iteritems():
			if x > v:
				table[k] = x
			elif x > k and x < v:
				return True
	return False

inputs = [
	[1, 2, 3, 4],
	[3, 1, 4, 2],
	[-1, 3, 2, 0]
]

for i in inputs:
	print "%s : %s" % (i, seq_slow(i))








