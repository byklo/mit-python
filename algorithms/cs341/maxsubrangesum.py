import random
from timer import Timer

# MAX SUBRANGE SUM PROBLEM
# given a list of n integers, find the subsequence with the greatest sum

def naive(a):
# enumerate all possibilities
# O(n^2)
	max_sum = 0
	for start in xrange(len(a)):
		cur_sum = 0
		for subsequence_index in xrange(len(a) - start):
			cur_sum += a[start + subsequence_index]
			max_sum = max(max_sum, cur_sum)
	return max_sum

def rs_preprocess(a):
# preprocess a with a running sum array where rs[i] = sum(a[0..i])
# O(n^2)
	# rs is made in O(n) time
	# initialize rs as an array - size n+1
	rs = [ 0 for x in xrange(len(a) + 1) ]
	rs[0] = 0
	for i in xrange(len(a)):
		rs[i+1] = rs[i] + a[i]

	max_sum = 0

	for start in xrange(len(a)):
		cur_sum = 0
		for subsequence_end in xrange(start, len(a)):
			cur_sum = rs[subsequence_end + 1] - rs[start]
			max_sum = max(max_sum, cur_sum)
	return max_sum

def recursive(a):
# split a in half, the max is either in left, right or straddles the middle
# if it straddles the middle, then it is the greatest suffix of the left + the greatest prefix of the right
# T(n) = 2T(n/2) + n = O(n lg n)
	if len(a) == 1:
		return a[0]
	else:
		m = len(a) / 2

		left_max = recursive(a[0:m])
		right_max = recursive(a[m:len(a)])
		cur_max = max(left_max, right_max)

		# calculate max_middle for O(n)
		max_suffix = 0
		cur_suffix = 0
		for i in xrange(m):
			cur_suffix += a[m - 1 - i]
			max_suffix = max(max_suffix, cur_suffix)

		max_prefix = 0
		cur_prefix = 0
		for i in xrange(len(a) - m):
			cur_prefix += a[m + i]
			max_prefix = max(max_prefix, cur_prefix)

		max_middle = max_suffix + max_prefix
		cur_max = max(cur_max, max_middle)
		return cur_max

def linear(a):
# moving through the array, the maximum subsequence is either
#	1 - passed
#	2 - the sum of some suffix seen with the new element
# O(n)
	max_suffix = 0
	cur_max = 0
	for i in xrange(len(a)):
		max_suffix = max(0, max_suffix + a[i])
		cur_max = max(cur_max, max_suffix)
	return cur_max

a = random.sample(xrange(-100000, 100000), 5000)
timer = Timer()

# print a

timer.start("naive")
print naive(a)
timer.end()

timer.start("rs_preprocess")
print rs_preprocess(a)
timer.end()

timer.start("recursive")
print recursive(a)
timer.end()

timer.start("linear")
print linear(a)
timer.end()