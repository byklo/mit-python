# implement a linked list with insert() and remove()

import sys

class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def insert(self, x):
		if self.head is None:
			self.head = Node(x)
		else:
			cur = self.head
			while (cur.next is not None):
				cur = cur.next
			cur.next = Node(x)

	def show(self):
		cur = self.head
		while (cur is not None):
			sys.stdout.write("%s -> " % cur.val)
			cur = cur.next
		print ""

	def remove(self, x):
		if self.head is None:
			return
		elif self.head.val == x:
			self.head = self.head.next
		else:
			# in middle or tail
			prev = self.head
			cur = prev.next
			while (cur is not None):
				if cur.val == x:
					prev.next = cur.next
					break
				else:
					prev = cur
					cur = cur.next
		return

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)

ll.show()

ll.remove(4)

ll.show()

ll.remove(6)

ll.show()

ll.remove(1)

ll.show()

ll.insert(77)

ll.show()