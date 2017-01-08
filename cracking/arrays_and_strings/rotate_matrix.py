# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?

import numpy as np

def rotated_with_copy(matrix):
	# n x n matrix
	# O(n^2) solution using O(n^2) space
	# rotates clockwise
	n = matrix.shape[0]
	rotated_matrix = np.zeros((n, n))
	for i in xrange(n):
		for j in xrange(n):
			rotated_matrix[j][n - i - 1] = matrix[i][j]
	return rotated_matrix

def rotated_in_place(matrix):
	# O(n^2) solution using O(1) space
	# rotates clockwise
	n = matrix.shape[0]
	for d in xrange(n/2):
		for i in xrange(d, n - d - 1):
			corners = [ matrix[d][i], matrix[n - i - 1][d], matrix[n - d - 1][n - i - 1], matrix[i][n - d - 1] ]
			matrix[i][n - d - 1] = corners[0]
			matrix[d][i] = corners[1]
			matrix[n - i - 1][d] = corners[2]
			matrix[n - d - 1][n - i - 1] = corners[3]
	return matrix

matrices = [ np.arange(16).reshape(4, 4), np.arange(9).reshape(3, 3) ]

rotated = rotated_in_place

for matrix in matrices:
	print "original:"
	print matrix
	print "rotated:"
	print rotated(matrix)