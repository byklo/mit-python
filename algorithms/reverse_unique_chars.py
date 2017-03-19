# reverse unique chars
# given aaabbc, return cba
# aabbc -> abc -> cba

def ruc(string):
	output = ""
	uniques = {}
	for c in string:
		if c not in uniques:
			output = c + output
			uniques[c] = 1
	return output

tests = [
	"aabc",
	"cccbaaaa",
	"aggg1o"
]

for s in tests:
	print "%s -> %s" % (s, ruc(s))