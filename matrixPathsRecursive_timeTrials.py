import numpy as np
import time

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
	
	
def singleRun():
	start = time.time()
	numPaths(0,0)
	return time.time() - start

def main():
	global rows, columns

	# trials per graph size
	trials = 10

	# percent of matrix cells blocked
	blockPercent = 0.1

	# want input sizes of 2^k for k in {4, 5, ..., 12}
	# easy to do 2^2, 4^2, 8^2, ... 64^2 (same as 2^2, 2^4, 2^6, ... 2^12)
	for power in range(1, 9):
		dimension = 2**power

		processTime = 0
		for t in range(trials):
			rows = dimension
			columns = dimension
			setUpBlockMatrix(blockPercent)
			setUpCostMatrix()
			processTime += singleRun()

		print "n: ", dimension**2, " Average process time: ", processTime/trials	

if __name__ == '__main__':
		main()