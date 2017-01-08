# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

import numpy as np

def zeroed(matrix):
	# m x n matrix
	# O(mn) solution - must O(mn) iterate to find zeros, then iterate again to zero out stuff
	m = matrix.shape[0]
	n = matrix.shape[1]
	rows = []
	cols = []
	for i in xrange(m):
		for j in xrange(n):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)
	for i in rows:
		for j in xrange(n):
			matrix[i][j] = 0
	for i in xrange(m):
		for j in cols:
			matrix[i][j] = 0
	return matrix

test_matrices = [ np.arange(16).reshape(4, 4), np.arange(9).reshape(3, 3), np.arange(15).reshape(3, 5) ]
test_matrices[0][2][1] = 0
test_matrices[1][2][2] = 0
test_matrices[2][1][3] = 0

for matrix in test_matrices:
	print "original:"
	print matrix
	print "zeroed:"
	print zeroed(matrix)