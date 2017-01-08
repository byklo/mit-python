# Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n-pairs of parentheses.

import random

def parens(pre, n, close):
	if n == 0 and close == 0:
		print pre
	else:
		if n == 0:
			parens(pre + ")", n, close - 1)
		elif n == close:
			parens(pre + "(", n - 1, close)
		elif n < close:
			parens(pre + "(", n - 1, close)
			parens(pre + ")", n, close - 1)
	# TIME
	#	should technically grow at the same rate as Catalan numbers
	#	exponential
	#	i think O(4^n)

def parens_return(pre, n, close, ret):
	if n == 0 and close == 0:
		ret.append(pre)
	else:
		if n == 0:
			parens_return(pre + ")", n, close - 1, ret)
		elif n == close:
			parens_return(pre + "(", n - 1, close, ret)
		elif n < close:
			parens_return(pre + "(", n - 1, close, ret)
			parens_return(pre + ")", n, close - 1, ret)

n = random.randint(1, 5)
print "n = %s" % n
parens("", n, n)

ret = []
parens_return("", n, n, ret)
print len(ret)