class Rapper:
	'This is a rapper class'
	# rapperCount is a STATIC variable
	# access it with Rapper.rapperCount
	rapperCount = 0

	def __init__(self, name, latest_album):
		self.name = name
		self.latest_album = latest_album
		# static...
		Rapper.rapperCount += 1

	def getRapperCount(self):
		return Rapper.rapperCount
	
	def info(self):
		print "%s's latest album is %s" % (self.name, self.latest_album)

kendrick = Rapper("Kendrick Lamar", "To Pimp A Butterfly")
jcole = Rapper("J. Cole", "2014 Forest Hills Drive")

kendrick.info()

print kendrick.getRapperCount()

# you can dynamically add/remove/modify attributes on objects at any time

kendrick.age = 28

kendrick.info()

print "Kendrick is %s years old" % kendrick.age

del kendrick.age

# you get the following functions FOR FREE
#	- getattr(obj, name)
#	- hasattr(obj, name)
#	- setattr(obj, name, value)
#	- delattr(obj, name)

print "kendrick has a name?", hasattr(kendrick, 'name')
print "kendrick has an age?", hasattr(kendrick, 'age')

# returns a json-like map of an object
print kendrick.__dict__

# returns the doc string or if undefined, 'None'
print kendrick.__doc__

print kendrick.__class__.__name__

del kendrick

# kendrick.info()

# __del__() is a DESTRUCTOR. it has to be defined
# it is ALWAYS called when an instance is destroyed, even upon program exit
# calling __del__() doesn't actually destruct (destroy) the instance, it just executes the code inside __del__ block

class Car:
	def __init__(self, model, year):
		self.model = model
		self.year = year
		print "Created %s(%s, %s)" % (self.__class__.__name__, model, year)

	def info(self):
		print "Hi, I am a %s %s" % (self.year, self.model)

	def __del__(self):
		class_name = self.__class__.__name__
		print "Destroyed %s(%s, %s)" % (class_name, self.model, self.year)

bmw = Car("E30 M3", "1985")

bmw.info()

print "do something"

bmw.__del__()

bmw.info()

print "done"

del bmw

print "actually done now"

porsche = Car("Porsche 930", "1988")

print repr(porsche)
print str(porsche)

# you can define behaviour for adding (using the + operator)

# you can make 'private' variables by prefixing them with "__"
