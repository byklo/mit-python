# validate binary search tree ordering property on a valid tree

class TreeNode(object):
	def __init__(self, _key=None, _value=None):
		self.key = _key
		self.value = _value
		self.left = None
		self.right = None


def validate(head):
	if head is None:
		return True
	else:
		value = validate(head.left) and validate(head.right)
		value &= True if head.left is None else head.key > head.left.key
		value &= True if head.right is None else head.key < head.right.key
		return value


# NOT THE TEST TREE
#                 -1
#          0              1
#      2       3      4       5
#     6 7     8 9   10

heads = []

# good
head = TreeNode(5)
head.left = TreeNode(3)
head.right = TreeNode(7)

heads.append( (head, True) )

# bad
head = TreeNode(5)
head.left = TreeNode(7)
head.right = TreeNode(3)

heads.append( (head, False) )

# bad
head = TreeNode(5)
head.left = TreeNode(3)
head.left.left = TreeNode(4)
head.right = TreeNode(7)

heads.append( (head, False) )

# good
head = TreeNode(5)
head.left = TreeNode(3)
head.left.left = TreeNode(2)
head.left.right = TreeNode(4)
head.right = TreeNode(7)

heads.append( (head, True) )

for head,exp in heads:
	print "Pass" if validate(head) == exp else "Fail"