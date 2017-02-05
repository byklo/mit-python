# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# 
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# 
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
#
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# 
# In this case, no transaction is done, i.e. max profit = 0.

import random

# O(n^2) solution, keep table of profits for each buy price
def max_profit_table(data):
	profit_table = {}
	max_profit = 0
	for x in data:
		profit_table[x] = 0
		for c,p in profit_table.iteritems():
			profit_table[c] = max(p, x - c)
			max_profit = max(max_profit, profit_table[c])
	return max_profit

# O(n) solution, smart book keeping
def max_profit(data):
	max_profit = 0
	current_min = float('inf')
	for x in data:
		if x < current_min:
			current_min = x
		else:
			max_profit = max(max_profit, x - current_min)
	return max_profit


data = random.sample(xrange(20), 10)

print "data : %s" % data
print "max_profit : %s" % max_profit(data)