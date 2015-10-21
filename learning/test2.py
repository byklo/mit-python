artist = "J. Cole"
num = 4
album = "2014 Forest Hills Drive"
x = "Kendrick has %d studio albums released under %s" % (4, "TDE")
y = "%s %dth album is called %s" % (artist, num, album)

print x
print y

print "I said - r: %r" % x
print "I said - s: %s" % x
print "I said - r: %r" % y
print "I said - s: %s" % y

bol = True
z = "Kendrick is the best : %r"

print z % bol

concat1 = "kendrick"
concat2 = "dabest"

print concat1, concat2
