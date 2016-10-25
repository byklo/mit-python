import random

letters = [
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
		for x in letters[numbers[i]]:
			temp = pre
			temp += x
			printperms(numbers, i+1, temp)

numbers = [ random.choice(xrange(0, 7)) for x in xrange(10) ]

printperms(numbers, 0, '')
