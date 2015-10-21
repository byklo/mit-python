line = "Kendrick Lamar, by far, realest negus alive."

print line
print len(line)
print line.index("g")
print line.index("Lamar")
print line.count("a")
print line.count("ar")

# slice

print line[0:9]
print line[:9]
print line[34:]

# you can use negative numbers

print line[-5:]

print line.upper()
print line.lower()

if line.startswith("Kendrick"):
	print 'Line starts with "Kendrick"'

if line.endswith("dick."):
	print 'Line ends with "dick."'
else:
	print 'Line does not end with "dick."'

# splits generate a list

splits = line.split(" ")

print splits
