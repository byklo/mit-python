# reverse a linked list

import sys

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

def print_ll(head):
	cur = head
	while (cur is not None):
		sys.stdout.write("%s -> " % cur.val)
		cur = cur.next
	print ""

def reverse_ll(head):
	values = []
	cur = head
	while (cur is not None):
		values.append(cur.val)
		cur = cur.next
	cur = head
	while (cur is not None):
		cur.val = values.pop()
		cur = cur.next


head = Node(0)
cur = head
for i in xrange(1, 6):
	cur.next = Node(i)
	cur = cur.next

print_ll(head)

reverse_ll(head)

print_ll(head)