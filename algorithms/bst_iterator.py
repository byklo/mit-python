# 173 Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Definition for a  binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BSTIterator(object):
	def __init__(self, root):
		self.cur = root
		self.stack = []
		if root is None:
			return
		while (self.cur is not None):
			self.stack.append(self.cur)
			self.cur = self.cur.left
		self.cur = self.stack.pop()

	def hasNext(self):
		return self.cur is not None or len(self.stack) > 0

	def next(self):
		ret_node = self.cur
		if self.cur.right is not None:
			self.cur = self.cur.right
			while (self.cur is not None):
				self.stack.append(self.cur)
				self.cur = self.cur.left
			self.cur = self.stack.pop()
		else:
			self.cur = None
			if len(self.stack) > 0:
				self.cur = self.stack.pop()
		return ret_node.val


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)

i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())

print v