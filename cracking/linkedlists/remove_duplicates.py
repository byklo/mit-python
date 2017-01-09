# Write code to remove duplicates from an unsorted linked list.

import Node

def remove_duplicates(head):
	# O(n) - iterate once to build a counter of number of duplicates for each value
	# then go through the list again, remove a node if the number of duplicates is greater than 1,
	# decrement number of duplicates on removal
	duplicate_counter = {}
	cur = head
	while cur is not None:
		value = cur.value
		if duplicate_counter.has_key(value):
			duplicate_counter[value] += 1
		else:
			duplicate_counter[value] = 0
		cur = cur.next
	new_head = head
	cur = new_head
	prev = None
	while cur is not None:
		value = cur.value
		if duplicate_counter[value] > 0:
			if cur is new_head:
				new_head = cur.next
				cur = new_head
			else:
				prev.next = cur.next
				cur = cur.next
			duplicate_counter[value] -= 1
		else:
			prev = cur
			cur = cur.next
	return new_head


values = [ 5, 2, 3, 1, 4, 3, 3, 4, 5 ]

head = Node.make_ll(values)
print "original:"
Node.print_ll(head)
print "duplicates removed:"
head2 = remove_duplicates(head)
Node.print_ll(head2)