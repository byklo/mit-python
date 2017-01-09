# Implement a function to check if a linked list is a palindrome.

import Node

def is_palindrome(head):
	values = []
	cur = head
	while cur is not None:
		values.append(cur.value)
		cur = cur.next
	ret = True
	for i in xrange(len(values)):
		ret &= values[i] == values[len(values) - 1 - i]
	return ret

test_strings = [ "palindrome", "aabaa", "agga" ]

for string in test_strings:
	string_ll = Node.make_ll(string)
	print "%s %s a palindrome!" % (string, "is" if is_palindrome(string_ll) else "is not")