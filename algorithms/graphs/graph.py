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
	
	def addNode(self, value):
		if not self.hasNode(value):
			self.nodes.append(LinkedListNode(value))
		return
	
	def addEdge(self, v1, v2):
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
	
	def removeNode(self, rm_value):
		self.nodes.remove(LinkedListNode(rm_value))
		for node in self.nodes:
			cur = node
			while cur.next is not None:
				if cur.next.eq(rm_value):
					cur.next = cur.next.next
					break
		return


	def removeEdge(self, v1, v2):
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

	
	def hasNode(self, value):
		return LinkedListNode(value) in self.nodes
	
	def hasEdge(self, v1, v2):
		for node in self.nodes:
			if node.eq(v1):
				temp = node
				while temp is not None:
					if temp.eq(v2):
						return True
					temp = temp.next
		return False

	def getNodes(self):
		nodes = [ n.value for n in self.nodes ]
		return nodes

if __name__ == "__main__":
	g = AdjacencyList()
	g.addNode(5)
	g.addNode(7)
	g.addEdge(5, 7)
	print g.hasNode(7)
	print g.hasEdge(8, 7)
	print g.hasEdge(7, 5)










