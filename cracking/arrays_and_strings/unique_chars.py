# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def unique_chars(string):
	# LOG COST
	# O(n lg n) solution - sort strings, then O(n) scan for duplicate characters
	# You could have a O(n) solution using a hash table but that requires O(n) space, the sort solution can be done in place
	string = sorted(string)
	for i in xrange(1, len(string)):
		if string[i] == string[i-1]:
			return False
	return True

test_strings = [ "fail", "correct" ]

for s in test_strings:
	print "string \"%s\" %s unique characters" % (s, "has all" if unique_chars(s) else "does not have all")