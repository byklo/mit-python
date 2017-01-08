# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

def is_rotation(s1, s2):
	# just append one string with itself. if s1 is a rotation of s2, the repeated concatenation of s1 will
	# inherently contain s2
	repeated = s1 + s1
	return True if repeated.find(s2) > -1 else False

test_strings = [ ("waterbottle", "erbottlewat"), ("glenlivet", "livetglne") ]

for item in test_strings:
	print "%s and %s %s rotations of each other" % (item[0], item[1], "are" if is_rotation(item[0], item[1]) else "are not")