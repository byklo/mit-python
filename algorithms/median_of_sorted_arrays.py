# Median of 2 sorted arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/)
# 
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# 
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5

import random

def median(a, b):
	list_1 = list(a)
	list_2 = list(b)
	m = len(list_1)
	n = len(list_2)
	odd = (m + n) % 2 == 1
	median_value = None
	if odd:
		# return "center" element
		index = (m + n) / 2
		for i in xrange(index + 1):
			median_value = list_1.pop(0) if list_1[0] < list_2[0] else list_2.pop(0)
	else:
		# even - return average of the 2 center items
		index = (m + n) / 2
		median_indices = [ index - 1, index ]
		medians = []
		for i in xrange(index + 1):
			if not list_1:
				next_value = list_2.pop(0)
			elif not list_2:
				next_value = list_1.pop(0)
			else:
				next_value = list_1.pop(0) if list_1[0] < list_2[0] else list_2.pop(0)
			if i in median_indices:
				medians.append(next_value)
		median_value = (medians[0] + medians[1]) / 2.0
	return median_value

origin = sorted(random.sample(xrange(20), 10))
a = []
b = []
other = True
for x in origin:
	if other:
		a.append(x)
	else:
		b.append(x)
	other = other ^ True

a = [1, 2]
b = [3, 4]

print a
print b

print median(a, b)