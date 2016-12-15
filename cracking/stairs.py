# A child is running up a staircase with n steps,
# and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

import random

def count_rec(n):
	# idea: the child could arrive at the nth step using a 1 or 2 or 3 step hop
	#		count these three possibilities and their recursive counts
	if n < 0:
		# the step taken is not possible, possibility is not counted
		return 0
	if n == 0:
		# the previous 1/2/3 step fit perfectly, possibility is counted
		return 1
	else:
		# try all 1/2/3 step hops and sum the possibilities
		return count_rec(n - 1) + count_rec(n - 2) + count_rec(n - 3)
	# TIME
	#	each call makes 3 calls
	#	T(n) = T(n-1) + T(n-2) + T(n-3) <= 3T(n-1) = O(3^n)

def count_dp(n):
	# the recurrence, count[i] = number of ways to run up i steps
	#	count[i] = 0										if i < 0
	#	count[i] = 1										if i = 0
	#	count[i] = count[i-1] + count[i-2] + count[i-3]		if i > 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	count = [ 0 for x in xrange(n+1) ]
	count[0] = 1
	count[1] = 1
	count[2] = 2
	for i in xrange(3, n+1):
		count[i] = count[i-1] + count[i-2] + count[i-3]
	return count[n]
	# TIME = O(n)

n = random.randint(1, 10)
print n
print count_rec(n)
print count_dp(n)