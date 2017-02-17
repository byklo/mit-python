# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# 
# For example:
# 
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

import random

def weirdsum(n):
	digit = 0
	for x in str(n):
		digit += int(x)
		digit = digit - 9 if digit > 9 else digit
	return digit

n = random.randint(0, 99999)

print n

print weirdsum(n)