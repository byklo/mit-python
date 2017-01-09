import sys

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
	def has_next(self):
		return self.next is None

def print_ll(head):
	if head is None:
		return
	sys.stdout.write("%s" % head.value)
	n = head.next
	while n is not None:
		sys.stdout.write(" -> %s" % n.value)
		n = n.next
	sys.stdout.write("\n")

def make_ll(values):
	head = None
	tail = None
	for x in values:
		if head is None:
			head = Node(x)
			tail = head
		else:
			n = Node(x)
			tail.next = n
			tail = n
	return head