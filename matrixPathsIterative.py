import numpy as np
import time

# M * N matrix
# rows = 0
# columns = 0

def setUpBlockMatrix(numRows, numCols, blockPercent):
	global rows, columns
	rows = numRows
	columns = numCols
	# blockMatrix = np.zeros((rows, columns))
	#blockMatrix = np.random.randint(2, size=(5, 7))

	# Create blockMatrix with blockPercent random blocks
	blockMatrix = np.random.randint(1/blockPercent, size=(rows, columns))
	blockMatrix = blockMatrix < 1
	# Set beginning and end to unblocked
	blockMatrix[0][0] = False
	blockMatrix[rows-1][columns-1] = False
	#set the block values as 1 in the blockMatrix. 
	# blockMatrix[0][4] = 1
	# blockMatrix[2][1] = 1
	# blockMatrix[2][4] = 1
	# blockMatrix[3][1] = 1
	# blockMatrix[3][3] = 1
	# blockMatrix[3][6] = 1
	return blockMatrix	

def setUpCostMatrix():
	global rows, columns
	costMatrix = np.zeros((rows, columns))
	return costMatrix


def numOfPaths(blockMatrix, costMatrix): 
	global rows, columns

	# Set End to 1
	costMatrix[rows-1][columns-1] = 1
	# Set bottom row
	for j in range(columns-2, -1, -1):
		if blockMatrix[rows-1][j+1] == False:
			costMatrix[rows-1, j] = costMatrix[rows-1][j+1]
	for i in range(rows-2, -1, -1):
		if blockMatrix[i][columns-1] == False:
			costMatrix[i, columns-1] = costMatrix[i+1][columns-1]

	for i in range(rows-2, -1, -1):
		for j in range(columns-2, -1, -1):
			cost = 0
			if blockMatrix[i+1, j] == False:
				cost = costMatrix[i+1, j]
			if blockMatrix[i, j+1] == False:
				cost += costMatrix[i, j+1]
			costMatrix[i, j] = cost
	return costMatrix

def main():

	#if you want result of the above matrix, use the following:
	numRows = 8
	numCols = 8
	blockPercent = 0.1

	start = time.time()
	resultMatrix = numOfPaths(setUpBlockMatrix(numRows, numCols, blockPercent), setUpCostMatrix())
	end = time.time()

	print resultMatrix
	print "Total Paths: ", resultMatrix[0][0]
	print "Process time: ", end - start

	# numOfPaths(setUpMatrix(), setUpCostMatrix())

if __name__ == '__main__':
	main()