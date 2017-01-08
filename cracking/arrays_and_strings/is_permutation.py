# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2):
	# LOG COST
	# O(n lg n) solution - just sort the strings and O(n) compare
	# Can be done in O(n) using a hash table but requires O(n) space
	s1 = sorted(s1)
	s2 = sorted(s2)
	return True if s1 == s2 else False

test_data = [ ("reap", "pear"), ("jest", "test") ]

for t in test_data:
	print "%s and %s %s permutations of each other" % (t[0], t[1], "are" if is_permutation(t[0], t[1]) else "are not")