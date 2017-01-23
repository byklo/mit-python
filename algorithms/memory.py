# memory allocator
# memory is byte addressable
# word is 4 bytes = 32 bits
# allocation only gives a single block

import sys
import random

# LINKED LIST IMPLEMENTATION
#	O(1) allocate - just get head from free list
#	O(1) release - blindly add the address back to free list

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Memory(object):
	def __init__(self, start, end, block_size):
		self.start = start
		self.block_size = block_size
		# make free list
		head = None
		cur = None
		while start < end:
			if head is None:
				head = Node(start)
				cur = head
			else:
				node = Node(start)
				cur.next = node
				cur = cur.next
			self.end = start
			start += block_size
		self.free_list = head

	def allocate(self):
		# get next free block, return address
		if self.free_list is None:
			# free_list empty
			return None
		else:
			# free_list not empty
			node = self.free_list
			self.free_list = node.next
			node.next = None
			return node.value

	def release(self, address):
		# check address in bounds
		if address < self.start or address > self.end:
			raise ValueError("mem error: release address %s out of bounds" % address)
		# check address is aligned
		if address % 4 != 0:
			raise ValueError("mem error: release address %s not aligned" % address)
		node = Node(address)
		node.next = self.free_list
		self.free_list = node

	def print_free(self):
		cur = self.free_list
		while cur is not None:
			sys.stdout.write("%s -> " % cur.value)
			cur = cur.next
		sys.stdout.write("NULL\n")

# k = random.randint(10, 20)
k = 5
block_size = 4

start_address = 0
end_address = 2 ** k - 1
n_blocks = 2 ** k / block_size


mem = Memory(start_address, end_address, block_size)
print "MEM [ %s .. .. %s ]" % (start_address, end_address)
mem.print_free()
print "%s blocks available" % n_blocks

# print "\nafter allocating a1, a2, a3 and releasing a1, a3:"
# a1 = mem.allocate()
# a2 = mem.allocate()
# a3 = mem.allocate()
# mem.release(a1)
# mem.release(a3)
# mem.print_free()

# print "\ntry releasing an out of bounds address"
# try:
# 	mem.release(-1)
# except ValueError as e:
# 	print e

# print "\ntry releasing an unaligned address"
# try:
# 	mem.release(5)
# except ValueError as e:
# 	print e


# random test
operations = {
	"allocate" : mem.allocate,
	"release" : mem.release
}

used = []

for i in xrange(10):
	op = operations.keys()[random.randint(0, len(operations) - 1)]
	if op == "allocate":
		print "\nallocate()"
		used.append(operations[op]())
		mem.print_free()
	elif len(used) > 0:
		address = random.choice(used)
		print "\nrelease(%s)" % (address)
		used.remove(address)
		mem.release(address)
		mem.print_free()












