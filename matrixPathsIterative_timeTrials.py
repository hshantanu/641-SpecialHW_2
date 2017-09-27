import numpy as np
import time

# M * N matrix
# rows = 0
# columns = 0

def setUpBlockMatrix(numRows, numCols, blockPercent):
	global rows, columns
	rows = numRows
	columns = numCols

	# Create blockMatrix with blockPercent random blocks
	blockMatrix = np.random.randint(1/blockPercent, size=(rows, columns))
	blockMatrix = blockMatrix < 1

	# Set beginning and end to unblocked
	blockMatrix[0][0] = False
	blockMatrix[rows-1][columns-1] = False
	return blockMatrix	

def setUpCostMatrix():
	global rows, columns
	costMatrix = np.zeros((rows, columns))
	return costMatrix


def numOfPaths(blockMatrix, costMatrix): 
	global rows, columns

	# start timer
	start = time.time()

	# Set End to 1
	costMatrix[rows-1][columns-1] = 1

	# Calculate bottom row
	for j in range(columns-2, -1, -1):
		if blockMatrix[rows-1][j+1] == False:
			costMatrix[rows-1, j] = costMatrix[rows-1][j+1]
	# Calculate right column
	for i in range(rows-2, -1, -1):
		if blockMatrix[i][columns-1] == False:
			costMatrix[i, columns-1] = costMatrix[i+1][columns-1]

	# Calculate rest of matrix
	for i in range(rows-2, -1, -1):
		for j in range(columns-2, -1, -1):
			cost = 0
			if blockMatrix[i+1, j] == False:
				cost = costMatrix[i+1, j]
			if blockMatrix[i, j+1] == False:
				cost += costMatrix[i, j+1]
			costMatrix[i, j] = cost

	# return time to calculate
	return time.time() - start

def main():
	# trials per graph size
	trials = 10

	# percent of matrix cells blocked
	blockPercent = 0.1

	# want input sizes of 2^k for k in {4, 5, ..., 12}
	# easy to do 2^2, 4^2, 8^2, ... 64^2 (same as 2^2, 2^4, 2^6, ... 2^12)
	for power in range(1, 10):
		dimension = 2**power

		processTime = 0
		for t in range(trials):
			processTime += numOfPaths(setUpBlockMatrix(dimension, dimension, blockPercent), setUpCostMatrix())

		print "n: ", dimension**2, " Average process time: ", processTime/trials	


if __name__ == '__main__':
	main()