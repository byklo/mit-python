# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not
# become smaller than the original string, your method should return the original string.

def compress(string):
	# basically implementing run length encoding
	# maintain a list of "character encoding" tuples (character, run length)
	# LOG COST
	# O(n) solution - loop through string, building a list of char_encode objects, loop through char_encodes, build compressed string
	char_encodes = []
	prev = None
	count = 1
	for c in string:
		if c == prev:
			count += 1
		else:
			char_encodes.append( (prev, count) )
			prev = c
			count = 1
	char_encodes.append( (prev, count) )
	# construct compressed string
	compressed = ""
	for item in char_encodes[1:]:
		# skip first
		compressed += "%s%s" % (item[0], item[1])
	return compressed if len(compressed) < len(string) else string

test_strings = [ "non-compressable", "veeeeeerycooooooooooooooompressable" ]

for s in test_strings:
	print "%s was compressed to %s" % (s, compress(s))