# given a binary tree, print all right-most nodes (jake's a9 q)

class TreeNode(object):
	def __init__(self, _key=None, _value=None):
		self.key = _key
		self.value = _value
		self.left = None
		self.right = None

# incorrect; what if right most path cuts off while the levels continue on the left?
def print_right(head):
	current = head
	while current is not None:
		print current.key
		current = current.left if current.right is None else current.right
	return

# correct; the jake solution lol
# O(n) time, O(n) space
def print_right2(head):
	level_nodes = []
	level_nodes.append(head)
	next_level_nodes = []
	right_most = []
	while len(level_nodes):
		for i,x in enumerate(level_nodes):
			if x.left:
				next_level_nodes.append(x.left)
			if x.right:
				next_level_nodes.append(x.right)
			if i == len(level_nodes) - 1:
				# last
				right_most.append(x.key)
		level_nodes = next_level_nodes
		next_level_nodes = list()
	for r in right_most:
		print r
	return

head = TreeNode(-1)
n = 11

#                 -1
#          0              1
#      2       3      4       5
#     6 7     8 9   10

# pre  : -1 0 2 6 7 3 8 9 1 4 10 5
# in   : 6 2 7 0 8 3 9 -1 10 4 1 5
# post : 6 7 2 8 9 3 0 10 4 5 1 -1

level_parents = []
level_parents.append(head)
next_level_parents = []

for i in xrange(n):
	next_parent = level_parents.pop(0)
	if not next_parent.left:
		next_parent.left = TreeNode(i)
		next_level_parents.append(next_parent.left)
		level_parents.insert(0, next_parent)
	else:
		next_parent.right = TreeNode(i)
		next_level_parents.append(next_parent.right)
	if len(level_parents) < 1:
		level_parents = next_level_parents
		next_level_parents = []

print_right2(head)