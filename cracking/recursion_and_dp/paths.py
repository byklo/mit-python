# Imagine a robot sitting on the upper left comer of an X by Y grid.
# The robot can only move in two directions: right and down.
# How many possible paths are there for the robot to go from (0, 0) to (X, Y)?

import random

def paths_rec(x, y):
	# can write a recurrence for npaths[x,y] = number of paths from (0,0) to (x,y)
	#	npaths[x,y] = 0									if (x,y) = (0,0)
	#	npaths[x,y] = 1									if (x,y) = (1,0) or (x,y) = (0,1)
	#	npaths[x,y] = npaths[x-1,y] + npaths[x,y-1]		general case, consider reaching current spot with a down or a right and recurse
	if x < 0 or y < 0:
		return 0
	elif (x == 1 and y == 0) or (x == 0 and y == 1):
		return 1
	else:
		return paths_rec(x-1, y) + paths_rec(x, y-1)
	# TIME
	#	each call makes 2 calls = O(2^n)

def paths_dp(x, y):
	# use recurrence above, build ground up
	# npaths = 2D array size [x+1][y+1] (for zero)
	npaths = [ [ 0 for j in xrange(y+1) ] for i in xrange(x+1) ]
	# set base cases
	npaths[0][0] = 0
	npaths[1][0] = 1
	npaths[0][1] = 1
	npaths[1][1] = 2
	# we're gonna build a then b then c
	# 0 1 a |
	# 1 2 b |
	# a b c \/
	# ---->
	for border in xrange(2, max(x,y)+1):
		for sweep in xrange(border+1):
			# bottom left
			if border <= x and sweep <= y:
				# print "calculating (%s,%s)" % (border, sweep)
				if sweep == 0:
					npaths[border][sweep] = 1
				else:
					npaths[border][sweep] = npaths[border-1][sweep] + npaths[border][sweep-1]
			# upper right
			if border <= y and sweep <= x and border != sweep:
				# print "calculating (%s,%s)" % (sweep, border)
				if sweep == 0:
					npaths[sweep][border] = 1
				else:
					npaths[sweep][border] = npaths[sweep-1][border] + npaths[sweep][border-1]
	return npaths[x][y]
	# TIME = O(n^2)

# TESTS
# (5, 1) = 6
# (6, 2) = 28

x = random.randint(1, 10)
y = random.randint(1, 10)
print "grid is %s x %s" % (x, y)
print paths_rec(x, y)
print paths_dp(x, y)