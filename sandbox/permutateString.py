import sys

def permutate(pre, this):
	if len(this) == 1:
		print pre, this
	else:
		for char in this:
			permutate(pre + " " + char, this.replace(char, ""))

permutate("", sys.argv[1])
