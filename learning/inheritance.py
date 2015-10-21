class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print "Making person '%s' of age %s" % (name, age)

class Rapper(Person):
	def __init__(self, name, age, song):
		Person.__init__(self, name, age)
		self.song = song
		print "Making rapper '%s' of age %s with song '%s'" % (name, age, song)

dude = Person("Lovelle", "19")
kendrick = Rapper("Kendrick Lamar", "28", "Sing About Me")

print dude.__dict__
print kendrick.__dict__

print "is dude's class a subclass of kendrick's class? ", issubclass(dude.__class__, kendrick.__class__)
print "is kendrick's class a subclass of dude's class? ", issubclass(kendrick.__class__, dude.__class__)

print "is dude an instance of Rapper? ", isinstance(dude, Rapper)
print "is kendrick an instance of Person? ", isinstance(kendrick, Person)
