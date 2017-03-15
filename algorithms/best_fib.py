# best fib
# starting at 1

def fib_dp(x):
	dp = [ 0 for i in xrange(x + 1) ]
	dp[0] = 0
	dp[1] = 1
	for i in xrange(2, x + 1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[x]

def fib_iter(x):
	if x == 1:
		return 1
	prev = 0
	cur = 1
	for i in xrange(2, x + 1):
		temp = cur
		cur += prev
		prev = temp
	return cur

def fib_rec(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib_rec(x - 1) + fib_rec(x - 2)

test_values = range(1, 10)

for x in test_values:
	print "fib(%s) = %s" % (x, fib_dp(x))
	print "fib(%s) = %s" % (x, fib_iter(x))
	print "fib(%s) = %s" % (x, fib_rec(x))