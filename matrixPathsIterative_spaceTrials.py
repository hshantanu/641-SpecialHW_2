import numpy as np
import time
import resource

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

	# calculate memory usage
	usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

	# return memory
	return usage

def main():
	# trials per graph size (doesn't change for different trial sizes, but it does change between runs...)
	trials = 1

	# percent of matrix cells blocked
	blockPercent = 0.1

	# want input sizes of 2^k for k in {4, 5, ..., 12}
	# easy to do 2^2, 4^2, 8^2, ... 64^2 (same as 2^2, 2^4, 2^6, ... 2^12)
	lastSpace = 0
	for power in range(1, 10):
		dimension = 2**power

		processSpace = 0
		for t in range(trials):
			processSpace += numOfPaths(setUpBlockMatrix(dimension, dimension, blockPercent), setUpCostMatrix())

		avgProcessSpace = processSpace/trials
		print "n: ", dimension**2, " Average process space: ", avgProcessSpace, " Difference from last: ", avgProcessSpace - lastSpace
		lastSpace = avgProcessSpace

if __name__ == '__main__':
	main()