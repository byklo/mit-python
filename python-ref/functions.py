# define python functions using keyword "def" along with function name

def tuck():
	print "tuck"

tuck()

def tuck(name):
	print "tuck %s" % name

tuck("you")
tuck("meek mill")

# returning values

def tucked(tucker, tuckee):
	return "%s tucked %s" % (tucker, tuckee)

print tucked("drake", "meek mill")

# IMPORTANT: python is pass-by-object-reference.
# in pass-by-reference, the function and the caller both access the same object in the same memory location
# in pass-by-value, the function copies the value of the object passed; there are 2 objects with the same value
# in pass-by-object-reference (python), the function and the caller both have their individual boxes with the same value from the same memory location
#	pass-by-object-reference is more like a tagging system, where all variables with the same value are actually a bunch of tags pointing to the same memory location
#	this method is (should?) be memory efficient, because you don't allocate new memory for duplicate values

listA = [0]
listB = listA
listB.append(1)

print "listA : %s" % listA
print "listB : %s" % listB

# listA and listB both point to the same memory location

def dosmth(lista):
	lista.append(1)

def dosmthelse(lista):
	lista = [0,1]

listC = [0]
#dosmth(listC)
dosmthelse(listC)
print listC

# ^ above code,
#	- pass-by-reference
#		- dosmth WILL change listC
#		- dosmthelse WILL change listC
#	- pass-by-value
#		- dosmth WILL NOT change listC
#		- dosmthelse WILL NOT change listC
#	- pass-by-object-reference (python)
#		- dosmth WILL change listC
#		- dosmthelse WILL NOT change listC

# essentially, python is like java
