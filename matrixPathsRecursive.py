import numpy

# global variables
rows = 0 #m
cols = 0 #n
M

def NumPaths(B, i, j):
	if (i == rows - 1) and (j == cols - 1):
		return 1

	if (B[i][j] == True) or (i >= m) or (j >= n):
		return 0

	if M[i][j] < 0:
		M[i][j] = NumPaths(B, i+1, j) + NumPaths(B, i, j+1)
	
	return M[i][j]

def SolveNumPaths(B, rows, cols):
	global M = [[-1] * cols] * rows
	
