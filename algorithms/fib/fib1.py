import sys

def fib(k):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	else:
		return fib(k-1) + fib(k-2)

print fib(int(sys.argv[1]))
