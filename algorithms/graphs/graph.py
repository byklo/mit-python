# implement graph as adjacency list AND adjacency matrix
# will implement undirected graphs

class LinkedListNode(object):
	def __init__(self, _value):
		self.value = _value
		self.next = None
	def __eq__(self, other):
		return self.value == other.value
	def __ne__(self, other):
		return not self.__eq__(other)
	def copy(self):
		return LinkedListNode(self.value)
	def eq(self, value):
		return self.value == value

class AdjacencyList(object):
	def __init__(self):
		self.nodes = []
	
	def add_node(self, value):
		if not self.has_node(value):
			self.nodes.append(LinkedListNode(value))
		return
	
	def add_edge(self, v1, v2):
		# assume nodes exist
		count = 2
		for node in self.nodes:
			if node.eq(v1):
				temp = node.next
				node.next = LinkedListNode(v2)
				node.next.next = temp
				count -= 1
			elif node.eq(v2):
				temp = node.next
				node.next = LinkedListNode(v1)
				node.next.next = temp
				count -= 1
			if count == 0:
				# quit early
				break
		return
	
	def remove_node(self, rm_value):
		self.nodes.remove(LinkedListNode(rm_value))
		for node in self.nodes:
			cur = node
			while cur.next is not None:
				if cur.next.eq(rm_value):
					cur.next = cur.next.next
					break
		return


	def remove_edge(self, v1, v2):
		for node in self.nodes:
			if node.eq(v1):
				temp = node
				while temp.next is not None:
					if temp.next.eq(v2):
						temp.next = temp.next.next
						break
			if node.eq(v2):
				temp = node
				while temp.next is not None:
					if temp.next.eq(v1):
						temp.next = temp.next.next
						break
		return

	
	def has_node(self, value):
		return LinkedListNode(value) in self.nodes
	
	def has_edge(self, v1, v2):
		for node in self.nodes:
			if node.eq(v1):
				temp = node
				while temp is not None:
					if temp.eq(v2):
						return True
					temp = temp.next
		return False

g = AdjacencyList()
g.add_node(5)
g.add_node(7)
g.add_edge(5, 7)
print g.has_node(7)
print g.has_edge(8, 7)
print g.has_edge(7, 5)










