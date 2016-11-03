import random

# O(n) solution with O(n) space complexity
def twosum(a, x):
	log = {}
	for i,y in enumerate(a):
		j = x - y
		if log.has_key(j):
			return (log[j], i)
		else:
			log[y] = i
	return None

a = random.sample(xrange(20), 5)
x = random.randint(0, 20)

print "Given array %s,\nare there any 2 elements that add up to %s?" % (a, x)
print twosum(a, x)
