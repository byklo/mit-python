# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.

import random

# same problem as the stairs i think
# no, not the same, order does not matter here
# there are only 2 ways to make 6 = (1+5) = (1*6)

def coin_memoize(n, combos, coins):
	# idea: recursion with memoization. each combo should be unique, disregarding coin order
	#		on base case, sort the coins, get a string, check against a hash table
	if n < 0:
		return 0
	elif n == 0:
		temp = sorted(coins)
		temp = [ str(x) for x in temp ]
		temp = ''.join(temp)
		if combos.has_key(temp):
			return 0
		else:
			combos[temp] = 1
			return 1
	else:
		return coin_memoize(n - 1, combos, list(coins) + [1]) + coin_memoize(n - 5, combos, list(coins) + [5]) + coin_memoize(n - 10, combos, list(coins) + [10]) + coin_memoize(n - 25, combos, list(coins) + [25])
	# TIME
	#	recursion + memoization.. hard to analyze
	#	i'd say we still try all possibilities so exponential
	#	O(4^n)

# not dp-able. because we are trying to enumerate "all possible" ways of doing something
# these problems should be inherently exponential bounded

# actually no, there IS a dp solution, uses the same idea as floyd-warshall
# https://andrew.neitsch.ca/publications/m496pres1.nb.pdf
# for test values
def coin_dp(n):
	denominations = [ 1, 5, 10, 25 ]
	denoms = len(denominations)

	ways = [ [ 0 for j in xrange(denoms) ] for i in xrange(n + 1) ]
	# ways[0..n][0..denoms-1]

	# init table
	# w[0][:] = 1
	# w[:][0] = 1
	for i in xrange(n + 1):
		ways[i][0] = 1
	for i in xrange(denoms):
		ways[0][i] = 1

	# the dp only checks ways[i][k-1], ways[i-x][k] AKA it only looks behind it.
	# so we can nest the loops both ways
	for k in xrange(1, denoms):
		for i in xrange(1, n + 1):
			without_current = ways[i][k - 1]
			with_current = ways[i - denominations[k]][k] if i - denominations[k] >= 0 else 0
			ways[i][k] = without_current + with_current
	return ways[n][denoms - 1]
	# TIME
	#	O(kn) where k = number of denominations


for i in xrange(0, 100, 5):
	# print "n = %s, ways = %s" % (i, coin_memoize(i, {}, ""))
	print "n = %s, ways = %s" % (i, coin_dp(i))
