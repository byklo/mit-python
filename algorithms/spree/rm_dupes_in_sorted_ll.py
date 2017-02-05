# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

import random

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def delete_duplicates(head):
	prev = None
	cur = head
	while cur is not None:
		if prev is not None and prev.val == cur.val:
			prev.next = cur.next
			cur = cur.next
		else:
			prev = cur
			cur = cur.next


a = sorted( random.sample(xrange(6), 4) + random.sample(xrange(6), 4) + random.sample(xrange(6), 4) )
print a

head = None
prev = None
cur = None
for x in a:
	cur = ListNode(x)
	if head is None:
		head = cur
	if prev is not None:
		prev.next = cur
	prev = cur

cur = head
while cur is not None:
	print cur.val
	cur = cur.next

print "delete dupes"
delete_duplicates(head)

cur = head
while cur is not None:
	print cur.val
	cur = cur.next