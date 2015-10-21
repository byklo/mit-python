# python has 2 loops, the for and the while

rappers = ["kendrick", "jcole", "drake", "earl", "tyler", "big krit", "big sean"]

for r in rappers:
	print "%s is one of my fav rappers doe" % r

# you can iterate over a sequence using "range" or "xrange"
#	range returns a list of numbers
#	xrange returns an iterator, it's more efficient
# note: python 3 uses range which is actually xrange.
# note2: (x)range is 0 based

for x in xrange(5):
	print x

for x in xrange(3, 5):
	print x

for x in xrange(0, 10, 2):
	print x

print "xxxxxxxxxxxxxxxxxxxxxxxx"

i = 0

# PYTHON DOESN'T USE i++ WTF

while i < 5:
	print i
	i += 1

print "xxxxxxxxxxxxxxxxxxxxxx"

t = 0

while t < 10:
	if t == 7:
		print "t" + " " + "i" + " " + "f" + " " + "f"
		break
	else:
		print t
	t += 1
	continue

print "xxxxxxxxxxxxxxxxxxxxxxx"

x = 4

while x < 20:
	# apparently this checks if its even !!!
	if x % 2 == 0:
		print x
	x += 1
