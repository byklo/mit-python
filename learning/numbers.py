# this is an integer
x = 5

# this is a float
y = 5.0
z = float(5)

print "x is %d and y is (%%d) %d" % (x, y)
print "x is %d and y is (%%s) %s" % (x, y)
print "x is %d and y is (%%f) %f" % (x, y)

# use %% to escape the percent sign

# strings can either be assigned with single or double quotes

string1 = 'this is string1'
string2 = "this is string2"

print "string1 is %s" % string1
print 'string2 is %s' % string2

print "x + y is %d" % (x + y)
print "string1 + string2 is %s" % (string1 + string2)

# simultaneous variable assignment

a, b = 5, 3

if a >= b:
	print "a(%d) is bigger or equal to b(%d)" % (a, b)

# print x + y + string1 <---- that won't work. can't mix types with operators unlike java
