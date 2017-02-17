# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 <= x, y < 231.
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#		 ^   ^
# 
# The above arrows point to positions where the corresponding bits are different.

import random

def dist(a, b):
	# take 2 ints as binary strings
	# xor them to find locations of different bits
	# count the 1's that represent differing bits
	# return sum
	return sum([ 1 for x in bin(a ^ b)[2:] if x == '1' ])

a = random.randint(0, 64)
b = random.randint(0, 64)

print a
print b

print dist(a, b)