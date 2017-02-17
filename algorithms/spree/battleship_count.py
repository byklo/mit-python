# Given an 2D board, count how many battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
# 
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically.
# In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
#
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
#
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
#
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?

def count_ships(table):
	rows = len(table)
	cols = len(table[0])

	copy_table = [ [0] + row + [0] for row in table ]
	copy_table.insert(0, [0] * (cols + 2))
	copy_table.append([0] * (cols + 2))

	count = 0
	last_row = {}
	cur_row = {}

	for n,row in enumerate(copy_table):
		tracker = 0
		for i,cell in enumerate(row):
			if cell == 1:
				tracker += 1
				cur_row[i] = True
			else:
				if tracker > 1:
					count += 1
					for j in xrange(i - tracker, i):
						del cur_row[j]
				if last_row.has_key(i):
					count += 1
				tracker = 0
		last_row = cur_row
		cur_row = {}
	return count

def count(table):
	n = len(table)
	m = len(table[0])
	count = 0
	for i,row in enumerate(table):
		for j,cell in enumerate(row):
			if cell == 1:
				# single case
				if (j - 1 < 0 or table[i][j-1] == 0) and (j + 1 == m or table[i][j+1] == 0) and (i - 1 < 0 or table[i-1][j] == 0) and (i + 1 == n or table[i+1][j] == 0):
					count += 1
				# horizontal cases
				elif j > 0 and table[i][j-1] == 1 and (j + 1 == m or table[i][j+1] == 0):
					count += 1
				# vertical case
				elif i > 0 and table[i-1][j] == 1 and (i + 1 == n or table[i+1][j] == 0):
					count += 1
	return count

tables = [
	# 3
	[
		[0,0,0,0],
		[1,1,0,1],
		[0,0,0,1],
		[1,1,0,1]
	],
	# 4
	[
		[0,0,0,0],
		[1,0,0,1],
		[0,0,0,1],
		[0,0,0,0],
		[0,1,0,1],
	],
]

table = [".X..X",".X..X","....X","X.XX.","X...X"]
table = [ [ 1 if x == "X" else 0 for x in list(row) ] for row in table ]

print count_ships(table)
print count(table)

# print table

for table in tables:
	print count_ships(table)









