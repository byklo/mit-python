# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

import Node
import random

def partition(x, head):
	l_head = None
	l_tail = None
	ge_head = None
	ge_tail = None
	cur = head
	prev = None
	while cur is not None:
		if cur.value < x:
			if l_head is None:
				l_head = cur
				l_tail = l_head
			else:
				l_tail.next = cur
				l_tail = cur
		else:
			if ge_head is None:
				ge_head = cur
				ge_tail = ge_head
			else:
				ge_tail.next = cur
				ge_tail = cur
		cur = cur.next
	# join
	if l_head is None:
		return ge_head
	elif ge_head is None:
		return l_head
	else:
		l_tail.next = ge_head
		ge_tail.next = None
		return l_head

ll_data = random.sample(xrange(10), random.randint(6, 7))
head = Node.make_ll(ll_data)
Node.print_ll(head)
k = random.randint(0, 10)
print "partitioning around k = %s" % k
head = partition(k, head)
Node.print_ll(head)