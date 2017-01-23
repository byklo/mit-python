import random

characters = [
	[ 'a', 'b', 'c' ],
	[ 'd', 'e', 'f' ],
	[ 'g', 'h', 'i' ],
	[ 'j', 'k', 'l' ],
	[ 'm', 'n', 'o' ],
	[ 'p', 'q', 'r', 's' ],
	[ 't', 'u', 'v' ],
	[ 'w', 'x', 'y', 'z' ]
]

def printperms(numbers, i, pre):
	if (i == len(numbers)):
		print pre
	else:
		for char in characters[numbers[i]]:
			temp = pre
			temp += char
			printperms(numbers, i+1, temp)

numbers = [ random.choice(xrange(0, 7)) for x in xrange(10) ]

printperms(numbers, 0, '')
