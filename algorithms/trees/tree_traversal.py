import sys

class TreeNode(object):
	def __init__(self, _key=None, _value=None):
		self.key = _key
		self.value = _value
		self.left = None
		self.right = None

def cout(string):
	sys.stdout.write(string)

# given tree
#            F
#       B         G
#    A     D         I
#         C E       H

# pre-order - print top down, left to right
# print, left, right
# F B A D C E G I H

# in-order - named because outputs search trees IN ORDER
# left, print, right
# A B C D E F G H I

# post-order - print bottom up, left to right
# left, right, print
# A C E D B H I G F


def pre_order_traverse_recursive(node):
	cout(str(node.key) + " -> ")
	if node.left is not None:
		pre_order_traverse_recursive(node.left)
	if node.right is not None:
		pre_order_traverse_recursive(node.right)

def in_order_traverse_recursive(node):
	if node.left is not None:
		in_order_traverse_recursive(node.left)
	cout(str(node.key) + " -> ")
	if node.right is not None:
		in_order_traverse_recursive(node.right)

def post_order_traverse_recursive(node):
	if node.left is not None:
		post_order_traverse_recursive(node.left)
	if node.right is not None:
		post_order_traverse_recursive(node.right)
	cout(str(node.key) + " -> ")

def pre_order_traverse_iterative(node):
	stack = []
	while len(stack) > 0 or node is not None:
		if node is None:
			# have reached an "edge" of the tree
			node = stack.pop()
		else:
			# value node of tree
			cout(str(node.key) + " -> ")
			stack.append(node.right)
			node = node.left

def in_order_traverse_iterative_original(node):
	# my idea was to use a stack for book keeping and a set to check for traversed nodes
	# i think in general, it's best to "iterate to null values" and somehow leverage them
	# for logic .. instead of doing what i do, checking for null values and avoiding them
	traversed = []
	stack = []
	stack.append(node)
	while len(stack) > 0:
		current_node = stack.pop()
		if current_node.left is not None and current_node.left not in traversed:
			stack.append(current_node)
			stack.append(current_node.left)
			continue
		if current_node not in traversed:
			cout(str(current_node.key) + " -> ")
			traversed.append(current_node)
			if current_node.right is not None and current_node.right not in traversed:
				stack.append(current_node.right)

def in_order_traverse_iterative(node):
	stack = []
	while len(stack) > 0 or node is not None:
		if node is None:
			node = stack.pop()
			cout(str(node.key) + " -> ")
			node = node.right
		else:
			stack.append(node)
			node = node.left

def post_order_traverse_iterative(node):
	traversed = []
	stack = []
	stack.append(node)
	while len(stack) > 0:
		node = stack.pop()
		if node.left is not None and node.left not in traversed or node.right is not None and node.right not in traversed:
			stack.append(node)
		else:
			cout(str(node.key) + " -> ")
			traversed.append(node)
		if node.right is not None and node.right not in traversed:
			stack.append(node.right)
		if node.left is not None and node.left not in traversed:
			stack.append(node.left)




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

print "pre order RECURSIVE"
pre_order_traverse_recursive(head)
print ""
print "pre order ITERATIVE"
pre_order_traverse_iterative(head)
print ""
print "in order RECURSIVE"
in_order_traverse_recursive(head)
print ""
print "in order ITERATIVE"
in_order_traverse_iterative(head)
print ""
print "post order RECURSIVE"
post_order_traverse_recursive(head)
print ""
print "post order ITERATIVE"
post_order_traverse_iterative(head)
print ""

