# reverse words

def rev(s):
	# in place
	string = list(s)
	# rev all
	n = len(string)
	for i in xrange(n / 2):
		temp = string[i]
		string[i] = string[n - 1 - i]
		string[n - 1 - i] = temp
	# rev words only
	left = 0
	right = 0
	while right < n:
		while (right < n and string[right] != ' '):
			right += 1
		right -= 1
		for i in xrange((right - left + 1)/2):
			temp = string[left + i]
			string[left + i] = string[right - i]
			string[right - i] = temp
		left = right + 2
		right += 2

	return ''.join(string)


tests = [ "ok tell me again", "what the quad", "help", "help please" ]

for s in tests:
	print "%s -> %s" % (s, rev(s))