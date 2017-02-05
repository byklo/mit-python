# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

import random

def max_subarray(a):
	max_suffix = float('-inf')
	max_sum = float('-inf')
	cur_start = 0
	cur_fin = 0
	max_start = 0
	max_fin = 0

	for i,x in enumerate(a):
		if max_suffix + x > x:
			max_suffix += x
			cur_fin = i
		else:
			max_suffix = x
			cur_start = i
			cur_fin = i

		if max_suffix > max_sum:
			max_sum = max_suffix
			max_start = cur_start
			max_fin = cur_fin

	return (a[max_start:max_fin + 1], max_sum)

a = random.sample(xrange(-10, 10), 6)

print a
print max_subarray(a)