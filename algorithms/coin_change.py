# You are given coins of different denominations and a total amount of money. Write a function
# to compute the number of combinations that make up that amount. You may assume that you have
# infinite # number of each kind of coin.
# 
# Note: You can assume that
# 
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# Example 1:
# 
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
# 
# Input: amount = 10, coins = [10] 
# Output: 1

# seems like an enumeration type of problem, considering recursion

import random

def count_memo(n, denom, memo={}):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		total = 0
		for i,d in reversed(list(enumerate(denom))):
			if n - d >= 0:
				if memo.has_key(str(n) + str(d) + str(denom[:i+1])):
					total += memo[str(n) + str(d) + str(denom[:i+1])]
				else:
					memo[str(n) + str(d) + str(denom[:i+1])] = count_memo(n - d, denom[:i+1], memo)
					total += memo[str(n) + str(d) + str(denom[:i+1])]
		return total


def count_dp(n, denom):
	# ahhh this is like fricken floyd warshall style solution
	dp = [ 0 for x in xrange(n+1) ]
	dp[0] = 1
	for d in denom:
		for i in xrange(n+1):
			if i >= d:
				dp[i] += dp[i - d]
	return dp[n]

# d = [ 2, 3 ]
# 0 1 2 3 4 5 6 7 8
# 1 0 1 0 1 0 1 0 1
# 1 0 1 1 1 1 2 1 2


base = 10
amount = random.randint(base, base*base)
# amount = 500
coins = sorted(random.sample(xrange(base), random.randint(2, base/2)))
# coins = [1,2,5]

print "amount : %s" % amount
print "coins : %s" % coins

print "combinations : %s" % count_dp(amount, coins)
