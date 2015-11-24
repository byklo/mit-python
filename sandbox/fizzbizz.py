#!/usr/bin/python

import sys

def fizzbizz(cap):
	for i in xrange(1, cap + 1):
		out = ""
		out += "Fizz" if i % 3 == 0 else ""
		out += "Bizz" if i % 5 == 0 else ""
		out += str(i) if not out else ""
		print out

fizzbizz(int(sys.argv[1]))
