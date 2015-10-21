import sys

def fib(k):
	if k == 0:
		return 0
	elif k == 1 or k == 2:
		return 1
	else:
		term1, term2 = 1, 1
		i = 2
		while (i < k):
			term1 += term2
			temp = term1
			term1 = term2
			term2 = temp
			i += 1
		return term2

print fib(int(sys.argv[1]))
