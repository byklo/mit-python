# 451. Given a string, sort it in decreasing order based on the frequency of characters.
# 
# Example 1:
# 
# Input:
# "tree"
# 
# Output:
# "eert"
# 
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
# 
# Input:
# "cccaaa"
# 
# Output:
# "cccaaa"
# 
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
# 
# Input:
# "Aabb"
# 
# Output:
# "bbAa"
# 
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

def char_sorted(string):
	char_count = {}
	for c in string:
		if char_count.has_key(c):
			char_count[c] += 1
		else:
			char_count[c] = 1
	return_string = ""
	for c,count in reversed(sorted(char_count.iteritems(), key=lambda x: x[1])):
		return_string += c * count
	return return_string

test_strings = [
	"tree",
	"cccaaa",
	"Aabb"
]

for string in test_strings:
	print "%s -> %s" % (string, char_sorted(string))