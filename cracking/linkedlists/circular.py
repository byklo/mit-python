# Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.

import Node

def get_cycle_start(head):
	slow = head.next
	fast = head.next.next
	while slow is not fast:
		slow = slow.next
		fast = fast.next.next
	fast = head
	while slow is not fast:
		slow = slow.next
		fast = fast.next
	return slow


ll_values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
ll = Node.make_ll(ll_values)
x = ll
y = ll
for i in xrange(4):
	y = y.next
while x.next is not None:
	x = x.next
x.next = y

bad_node = get_cycle_start(ll)

print "bad node starts at value : %s" % bad_node.value