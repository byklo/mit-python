# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

import Node
import random

def delete_middle(middle):
	cur = middle
	prev = None
	while cur.next is not None:
		if prev is None:
			prev = cur
			cur = cur.next
			continue
		prev.value = cur.value
		prev = cur
		cur = cur.next
	prev.value = cur.value
	prev.next = None

ll_data = random.sample(xrange(10), random.randint(6, 7))

head = Node.make_ll(ll_data)
Node.print_ll(head)

middle = head
for i in xrange(len(ll_data) / 2):
	middle = middle.next

delete_middle(middle)
Node.print_ll(head)