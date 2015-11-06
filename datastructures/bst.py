class BST:
	'''
	Binary search tree implementation assuming unique values
	'''
	def __init__(self):
		self.nodeCount = 0
		self.root = None
		self.nodes = []

	def insert(self, newValue):
		if self.nodeCount < 1:
			self.root = BSTNode(newValue)
			self.nodeCount += 1
			self.nodes.append(self.root)
		else:
			nextNode = self.root
			currentNode = None
			while nextNode:
				currentNode = nextNode
				currentNode.size += 1
				nextNode = currentNode.right if newValue > currentNode.value else currentNode.left
			newNode = BSTNode(newValue)
			newNode.parent = currentNode
			if newValue > currentNode.value:
				currentNode.right = newNode
			else:
				currentNode.left = newNode
			self.nodeCount += 1
			self.nodes.append(newNode)

	def nodesLessThan(self, value):
		count = 0
		nextNode = self.root
		currentNode = None
		while nextNode:
			currentNode = nextNode
			if currentNode.value > value:
				nextNode = currentNode.left
			else:
				count += 1
				if currentNode.left:
					count += currentNode.left.size
				nextNode = currentNode.right
		return count

	def min(self):
		nextNode = self.root
		currentNode = None
		while nextNode:
			currentNode = nextNode
			nextNode = currentNode.left
		return currentNode.value

	def max(self):
		nextNode = self.root
		currentNode = None
		while nextNode:
			currentNode = nextNode
			nextNode = currentNode.right
		return currentNode.value

	def info(self):
		print "// TREE INFO"
		print "\tnodeCount =", self.nodeCount
		print "\tmin =", self.min()
		print "\tmax =", self.max()
		print "\tinOrder =", self.toList()

	def printInOrder(self, currentNode=None):
		currentNode = currentNode if currentNode else self.root
		if currentNode.left:
			self.printInOrder(currentNode.left)
		print currentNode.value
		if currentNode.right:
			self.printInOrder(currentNode.right)
		return

	def toList(self, currentNode=None, array=None):
		array = array if array else [ None ]
		currentNode = currentNode if currentNode else self.root
		if currentNode.left:
			self.toList(currentNode.left, array)
		array.append(currentNode.value)
		if currentNode.right:
			self.toList(currentNode.right, array)
		return array[1:]

	def printNodes(self):
		for x in self.nodes:
			print "Node ->", x.value
			print "\tSize ->", x.size
			if x.parent:
				print "\tParent ->", x.parent.value
			if x.left:
				print "\tLeft ->", x.left.value
			if x.right:
				print "\tRight ->", x.right.value

class BSTNode:
	'''
	Binary search tree node implementation
	'''
	def __init__(self, value):
		self.value = value
		self.size = 1

		self.parent = None
		self.left = None
		self.right = None