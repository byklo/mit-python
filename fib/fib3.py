import sys

def fib(k, helper):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	elif helper.has_key(k):
		return helper.get(k)
	else:
		value = fib(k-1, helper) + fib(k-2, helper)
		helper[k] = value
		return value

fibdic = {}

print fib(int(sys.argv[1]), fibdic)
