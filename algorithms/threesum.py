import random

# O(n^2) solution with O(n) space complexity
def threesum(a, x):
	for i,y in enumerate(a):
		target = x - y
		log = {}
		for j,w in enumerate(a):
			if y == w:
				continue
			z = target - w
			if log.has_key(z):
				return (i, log[z], j)
			else:
				log[w] = j
	return None

a = random.sample(xrange(20), 10)
x = random.randint(0, 20)

print "Given array %s,\nare there any 3 elements that add up to %s?" % (a, x)
print threesum(a, x)
