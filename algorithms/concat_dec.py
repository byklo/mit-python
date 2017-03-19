# concat decimals
# given a, b, output a.b
# a = 20, b = 15, output = 20.15

import random
import math

def concat(a, b):
	result = a
	result += b / 10.0**(math.floor(math.log(b, 10))+1)
	return result

a = random.randint(0, 150)
b = random.randint(0, 150)

print "a : %s | b : %s | output : %.4f" % (a, b, concat(a, b))