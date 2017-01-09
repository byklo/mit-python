# Implement an algorithm to find the kth to last element of a singly linked list.

import Node
import random

def kthlast(k, head):
	n1 = head
	n2 = head
	for i in xrange(k - 1):
		n1 = n1.next
	while n1.next is not None:
		n1 = n1.next
		n2 = n2.next
	return n2

values = [ 1, 2, 3, 4, 5 ]

head = Node.make_ll(values)
print "linked list:"
Node.print_ll(head)
k = random.randint(1, len(values))
kth_last_element = kthlast(k, head)
print "%sth last element is %s" % (k, kth_last_element.value)