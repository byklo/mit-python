# check valid bracket string with {}, [] and ()
# with ordering properties, ie "([)]" is invalid

def check(string):
	stack = []
	b_type = {
		"{" : 0,
		"}" : 0,
		"[" : 1,
		"]" : 1,
		"(" : 2,
		")" : 2
	}
	is_open = {
		"{" : True,
		"(" : True,
		"[" : True
	}
	for b in string:
		if is_open.has_key(b):
			stack.append(b)
		else:
			if len(stack) and b_type[stack[-1]] == b_type[b]:
				# same, good
				stack.pop()
			else:
				# diff, out of order, fail
				return False
	return True if not len(stack) else False

tests = [
	("{{{}()}}", True),
	("{", False),
	("}", False),
	("()(){}[]]", False),
	("((((({}[])))))", True),
	("({[}])", False),
	("({[]})", True)
]

for test,exp in tests:
	assert check(test) == exp