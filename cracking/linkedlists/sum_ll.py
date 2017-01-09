# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1st digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.

import Node
import random

def add_ll(x, y):
	# assumes the linked lists are same length and will not "overflow"
	r = None
	tail = r
	carry = 0
	while x is not None and y is not None:
		temp = x.value + y.value + carry
		carry = 1 if temp > 9 else 0
		temp = temp - 10 if carry else temp
		if r is None:
			r = Node.Node(temp)
			tail = r
		else:
			temp = Node.Node(temp)
			tail.next = temp
			tail = tail.next
		x = x.next
		y = y.next
	return r

x = [ 7, 1, 6 ]
y = [ 5, 9, 2 ]

x = Node.make_ll(x)
y = Node.make_ll(y)

Node.print_ll(x)
print "+"
Node.print_ll(y)
print "====="
total = add_ll(x, y)
Node.print_ll(total)