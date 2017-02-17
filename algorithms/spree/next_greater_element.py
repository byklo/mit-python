# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element. The Next Greater Number of a number x is the
# first greater number to its traversing-order next in the array, which #means you could search
# circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
#
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.

import random

# TODO
# this does not work lol
# attempting a linear solution
def nge(a):
	a_w_indices = [ (a[i], i) for i in xrange(len(a)) ]
	a_w_indices.sort(key = lambda x : x[0])
	answer = [ -1 for i in xrange(len(a)) ]
	stack = []
	for x,i in reversed(a_w_indices):
		if len(stack) == 0:
			# first element
			answer[i] = -1
			stack.append((x,i))
		elif len(stack) == 1:
			answer[i] = stack[-1][0]
			stack.append((x,i))
		else:
			temp = None
			while len(stack) > 1 and i > stack[-1][1]:
				temp = stack.pop()
			answer[i] = stack[-1][0]
			if temp:
				stack.append(temp)
			stack.append((x,i))
	return answer

a = random.sample(xrange(20), 4)

print a
print nge(a)