import numpy as np

rows = 0 
columns = 0 
blockMatrix = None
costMatrix = None

def setUpBlockMatrix(blockPercent):
	global rows, columns, blockMatrix
	
	#blockMatrix = np.zeros((rows, columns))
	#blockMatrix = np.random.randint(2, size=(5, 7))

	# Create blockMatrix with blockPercent random blocks
	blockMatrix = np.random.randint(1/blockPercent, size=(rows, columns))
	blockMatrix = blockMatrix < 1
	# Set beginning and end to unblocked
	blockMatrix[0][0] = False
	blockMatrix[rows-1][columns-1] = False
	return None	

	
def setUpCostMatrix():
	global rows, columns, costMatrix
	costMatrix = np.zeros((rows, columns))
	costMatrix -= 1
	return None

def numPaths(i, j):
	global rows, columns, blockMatrix, costMatrix

	if (i == rows-1) and (j == columns-1) :
		return 1
		
	if (i >= rows) or (j >= columns) or (blockMatrix[i][j] == True):
		return 0
		
	if costMatrix[i][j]<0:
		costMatrix[i][j] = numPaths(i+1,j) + numPaths(i,j+1)
		
	return costMatrix[i][j]
	
	
'''def solveNumPaths(B,rows,cols):
	M = [[-1] * cols] * rows'''
	
def main():
	global rows, columns

	rows = 5
	columns = 5
	setUpBlockMatrix(0.1)
	setUpCostMatrix()
	
	print numPaths(0, 0)

if __name__ == '__main__':
		main()