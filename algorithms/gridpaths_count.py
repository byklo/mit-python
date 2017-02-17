# Imagine a robot sitting on the upper left comer of an X by Y grid.
# The robot can only move in two directions: right and down.
# How many possible paths are there for the robot to go from (0, 0) to (X, Y)?

# (1, 1) = 2
# (1, 2) = 3


def count_rec(x, y):
	if x == 0 and y == 0:
		return 1
	elif x < 0 or y < 0:
		return 0
	elif x > 0 or y > 0:
		return count_rec(x - 1, y) + count_rec(x, y - 1)

def count_dp(x, y):
	dp = [ [ 0 for j in xrange(y + 1) ] for i in xrange(x + 1) ]
	dp[0] = [ 1 for j in xrange(y + 1) ]
	for j in xrange(y + 1):
		for i in xrange(1, x + 1):
			dp[i][j] = dp[i-1][j] + dp[i][j-1] if j > 0 else dp[i-1][j]
	return dp[x][y]

grids = [ (1,1), (1,2), (2,1), (2,2), (4,5), (6, 4) ]

for x,y in grids:
	print count_rec(x, y)
	print count_dp(x, y)