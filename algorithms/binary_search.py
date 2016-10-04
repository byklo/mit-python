import random
import math

def binary_search(x, a):
	p = math.floor(len(a)/2)
	p = int(p)
	l = 0
	r = len(a) - 1

	while (a[p] != x and l < r):
		# print "p=%s l=%s r=%s" % (p, l, r)
		if a[p] < x:
			l = p + 1
		else:
			r = p - 1
		p = math.floor((r + l)/2)
		p = int(p)

	return True if (a[p] == x) else False

a = random.sample(xrange(0, 100), 14)
print a

a = sorted(a)
print a

x = random.randint(1, 99)

print "found %s? %s" % (x, binary_search(x, a))
