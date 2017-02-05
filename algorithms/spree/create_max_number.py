# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array # must be preserved.
# Return an array of the k digits. You should try to optimize your time and space complexity.
#
# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
#
# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]
#
# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]

import random

class TrieNode(object):
	def __init__(self, key):
		self.key = key
		self.children = []

def array_to_int(a):
	return int( ''.join( [ str(x) for x in a ] ) )

def int_to_array(x):
	return [ int(i) for i in list(str(x)) ]

def get_possible_k_nums(a, b, prefix_list, possible_nums, k):
	m = len(a)
	n = len(b)
	if k == 0:
		# base case
		possible_nums.append(array_to_int(prefix_list))
	else:
		a_copy = list(a)
		b_copy = list(b)
		pre_copy = list(prefix_list)
		# a[0] in
		if m > 0:
			item = a_copy.pop(0)
			pre_copy.append(item)
			get_possible_k_nums(a_copy, b_copy, pre_copy, possible_nums, k - 1)
		# a[0] out
			if m + n > k:
				get_possible_k_nums(a_copy, b_copy, list(prefix_list), possible_nums, k)

		a_copy = list(a)
		b_copy = list(b)
		pre_copy = list(prefix_list)
		# b[0] in
		if n > 0:
			item = b_copy.pop(0)
			pre_copy.append(item)
			get_possible_k_nums(a_copy, b_copy, pre_copy, possible_nums, k - 1)
		# b[0] out
			if m + n > k:
				get_possible_k_nums(a_copy, b_copy, list(prefix_list), possible_nums, k)
	return

def make_trie(head, a, b):
	a_copy = list(a)
	b_copy = list(b)
	if len(a) > 0:
		head.children.append(TrieNode(a_copy.pop(0)))
		make_trie(head.children[-1], a_copy, list(b))
	if len(b) > 0:
		head.children.append(TrieNode(b_copy.pop(0)))
		make_trie(head.children[-1], list(a), b_copy)
	return

def search_trie(head, k, current_max, current_value):
	# current_max is an single element array so we can pass by reference
	if len(current_value) < k:
		for child in head.children:
			search_trie(child, k, current_max, current_value + [child.key])
			search_trie(child, k, current_max, current_value)
	else:
		# len == k
		# compare to max, update
		current_num = array_to_int(current_value)
		current_max[0] = max(current_num, current_max[0])
		# if has children, continue
		if len(head.children) > 0:
			for child in head.children:
				search_trie(child, k, current_max, current_value[1:] + [child.key])
				search_trie(child, k, current_max, current_value[1:])
	return


######################################################################################################
# initial solutions, a recursive one and a trie-based one
def max_num(a, b, k):
	m = len(a)
	n = len(b)
	return_num = []

	# blind recursive solution
	# possible_nums = []
	# get_possible_k_nums(list(a), list(b), [], possible_nums, k)
	# num = max(possible_nums)
	# num = str(num)
	# num = list(num)
	# return num

	# trie solution, still slow :/
	head = TrieNode(None)
	make_trie(head, a, b)
	current_max = [0]
	search_trie(head, k, current_max, [])
	num = current_max[0]
	num = str(num)
	num = [ int(x) for x in num ]
	return num

######################################################################################################
# top solution
def top_soln(nums1, nums2, k):

    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]

    return max( merge(prep(nums1, i), prep(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2) )
######################################################################################################
# my solution lol
def max_k_single(a, k):
	if k == 0:
		return []
	stack = []
	for i,x in enumerate(a):
		if len(stack) > 0:
			if x > stack[-1]:
				while len(stack) > 0 and x > stack[-1] and (len(a) - i - 1) >= (k - len(stack)):
					stack.pop()
				stack.append(x)
			elif len(stack) < k:
				stack.append(x)
		else:
			stack.append(x)
	return stack

def max_merge(a, b):
	return [ max(a, b).pop(0) for x in xrange(len(a) + len(b)) ]

def max_k(a, b, k):
	longer = len(a)
	shorter = len(b)
	nums = []
	for i in xrange( max(k - longer, 0), min(shorter, k) + 1 ):
		nums.append( max_merge( max_k_single(a, k - i), max_k_single(b, i) ) ) 
	return max(nums)
######################################################################################################

MIN_LENGTH = 2
MAX_LENGTH = 10

m = random.randint(MIN_LENGTH, MAX_LENGTH)
n = random.randint(MIN_LENGTH, MAX_LENGTH)
k = random.randint(MIN_LENGTH, m + n)

print "m(%s), n(%s), k(%s)" % (m, n, k)

a = random.sample(xrange(10), m)
b = random.sample(xrange(10), n)

print "a : ", a
print "b : ", b

# trie solution works, but is exponential time :/
# print max_num(a, b, k)

# print top_soln(a, b, k)

print max_k(a, b, k)


