# LRU Cache (https://leetcode.com/problems/lru-cache/)
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a # new item.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class DLNode(object):
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None

class LRUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.table = {}
		self.queue_head = None
		self.queue_tail = None
		self.size = 0

	# head -----> prev_node -> node -> next_node -----> tail
	def get(self, key):
		if not self.table.has_key(key):
			return -1
		node = self.table[key]
		value = node.value
		# update queue
		next_node = node.next
		prev_node = node.prev
		if next_node is not None:
			next_node.prev = prev_node
		if prev_node is not None:
			prev_node.next = next_node
		if self.queue_tail is node and prev_node is not None:
			self.queue_tail = prev_node
		if self.queue_head is not None:
			self.queue_head.prev = node
			node.next = self.queue_head
			node.prev = None
			self.queue_head = node
		else:
			raise RuntimeError("get() thinks self.queue_head is None")
		return value

	def put(self, key, value):
		new_node = DLNode(key, value)
		self.table[key] = new_node
		if self.size == 0:
			# empty, first entry
			self.queue_head = new_node
			self.queue_tail = new_node
			self.size += 1
		elif self.size < self.capacity:
			# filling
			self.queue_head.prev = new_node
			new_node.next = self.queue_head
			self.queue_head = new_node
			self.size += 1
		else:
			# full, at full capacity
			# evict lru item
			lru_node = self.queue_tail
			self.queue_tail = lru_node.prev
			lru_node.prev.next = None
			lru_node.prev = None
			lru_node.next = None
			del self.table[lru_node.key]
			# insert new item
			self.queue_head.prev = new_node
			new_node.next = self.queue_head
			self.queue_head = new_node
		return

	def _print_dll(self):
		print "PRINTING"
		cur = self.queue_head
		while cur is not None:
			print "%s -> " % cur.value
			cur = cur.next
		print "TAIL = %s" % self.queue_tail.value
		return

cache = LRUCache(2)

cache.put(1, 1)
# cache._print_dll()
#	None -> 1 -> None
cache.put(2, 2)
# cache._print_dll()
#	None -> 2 -> 1 -> None

assert(cache.get(1) == 1)
# cache._print_dll()
#	None -> 1 -> 2 -> None

cache.put(3, 3)
# cache._print_dll()
#	None -> 3 -> 1 -> None

assert(cache.get(2) == -1)
# cache._print_dll()
#	None -> 3 -> 1 -> None

cache.put(4, 4)
# cache._print_dll()
#	None -> 4 -> 3 -> None

assert(cache.get(1) == -1)
# cache._print_dll()
#	None -> 4 -> 3 -> None
assert(cache.get(3) == 3)
# cache._print_dll()
#	None -> 3 -> 4 -> None
assert(cache.get(4) == 4)
# cache._print_dll()
#	None -> 4 -> 3 -> None

