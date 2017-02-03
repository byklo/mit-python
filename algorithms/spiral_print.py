def spiral_print(matrix, top_left, top_right, bottom_right, bottom_left):
	# print "top_left : ", top_left
	# print "top_right : ", top_right
	# print "bottom_right : ", bottom_right
	# print "bottom_left : ", bottom_left
	if top_left[1] > top_right[1]:
		# crossed corners, done
		return
	elif top_left == bottom_right:
		# there is a center item, print it
		print matrix[top_left[0]][top_left[1]]
		return
	elif top_left[1] == top_right[1] or top_left[0] == bottom_left[0]:
		# equal corners - reached a center line (vertical or horizontal)
		if top_left[1] == top_right[1]:
			# center vertical line
			# print top - down
			for i in xrange(top_left[0], bottom_left[0] + 1):
				print matrix[i][top_left[1]]
		else:
			# center horizontal line
			# print left - right
			for j in xrange(top_left[1], top_right[1] + 1):
				print matrix[top_left[0]][j]
	else:
		# valid corners
		for j in xrange(top_left[1], top_right[1]):
			print matrix[top_left[0]][j]
		for i in xrange(top_right[0], bottom_right[0]):
			print matrix[i][top_right[1]]
		for j in xrange(bottom_right[1], bottom_left[1], -1):
			print matrix[bottom_right[0]][j]
		for i in xrange(bottom_left[0], top_left[0], -1):
			print matrix[i][bottom_left[1]]
		spiral_print(
			matrix,
			(top_left[0] + 1, top_left[1] + 1),
			(top_right[0] + 1, top_right[1] - 1),
			(bottom_right[0] - 1, bottom_right[1] - 1),
			(bottom_left[0] - 1, bottom_left[1] + 1)
		)
	return

matrix_1 = [
	[ 0, 1, 2 ],
	[ 3, 4, 5 ],
	[ 6, 7, 8 ],
	[ 9, 10, 11 ]
]

matrix_2 = [
	[ 0, 1, 2 ],
	[ 3, 4, 5 ],
	[ 6, 7, 8 ]
]

matrix_4 = [
	[ 0, 1, 2, 3, 21],
	[ 4, 5, 6, 7, 14],
	[ 9, 10, 11, 12, 15]
]

print "PRINTING %s" % matrix_1
n = len(matrix_1)
m = len(matrix_1[0])
spiral_print(matrix_1, (0,0), (0, m - 1), (n - 1, m - 1), (n - 1, 0))

print "PRINTING %s" % matrix_2
n = len(matrix_2)
m = len(matrix_2[0])
spiral_print(matrix_2, (0,0), (0, m - 1), (n - 1, m - 1), (n - 1, 0))

print "PRINTING %s" % matrix_4
n = len(matrix_4)
m = len(matrix_4[0])
spiral_print(matrix_4, (0,0), (0, m - 1), (n - 1, m - 1), (n - 1, 0))