# pretty standard

# and == && , or == ||

myfavrapper = "kendrick"
herfavrapper = "chance"
myfavbeer = "sweetgrass"
herfavbeer = "flying"
myfavband = "the1975"
herfavband = "the1975"

if myfavrapper == herfavrapper:
	print "Our fav rapper is %s" % myfavrapper
else:
	print "We don't share a fav rapper"

if myfavbeer == herfavbeer:
	print "Our fav beer is %s" % myfavbeer
else:
	print "We don't share a fav beer"

if myfavband == "the1975" and herfavband == "the1975":
	print "Our fav band is %s" % myfavband
else:
	print "We don't share a fav band"

if myfavbeer == "sweetgrass" or myfavbeer == "rickards":
	print "my favourite beer is either %s or %s" % ("sweetgrass", "rickards")

# use "in" to see if an object exists in an iterable object container, like a list

if myfavrapper in ["xendrick", "hendrick", "hendrix"]:
	print "%s is in the list! yay!" % myfavrapper
# else if is "elif" WTF RIGHT??
elif myfavrapper == "kendrick" and herfavrapper == "chance":
	print "%s: maybe we have a %s" % (myfavrapper, herfavrapper)
else:
	print "you're stupid"

# you can evaluate if "exists" statements with if
# the following things will be evaluated as false
#	empty string, '', ""
#	empty list, []
#	number zero, 0
#	false

if myfavrapper:
	print "%s exists" % myfavrapper
else:
	print "myfavrapper does not exist"

# object instance match is done with keyword "is"

otherrapper = ["kendrick"]
otherotherrapper = ["kendrick"]

if not otherotherrapper is otherrapper:
	print "myfavrapper isssss kendrick!!!"
else:
	print "otherrapper is not otherotherrapper"

# "is" seems to work with any equal strings for some reason...

if "kendrick" is "kendrick":
	print "kendrick omg"
