import numpy as np

# M * N matrix
rows = 5
columns = 8

def setUpMatrix():
	global rows, columns	
	matrix = np.zeros((rows, columns))
	#matrix = np.random.randint(2, size=(5, 7))
	#set the block values as 1 in the matrix. 
	matrix[0][4] = 1
	matrix[2][1] = 1
	matrix[2][4] = 1
	matrix[3][1] = 1
	matrix[3][3] = 1
	matrix[3][6] = 1
	return matrix	

def setUpCostMatrix():
	global rows, columns
	costMatrix = np.zeros((rows, columns))
	return costMatrix


def numOfPaths(matrix, costMatrix): 
	global rows, columns
	for i in range(0, columns - 1):
		costMatrix[rows - 1, i] = 1
	for i in range(0, rows - 1):
		costMatrix[i, columns - 1] = 1

	for i in range(rows-2, -1, -1):
		for j in range(columns-2, -1, -1):
			cost = 0
			if matrix[i+1, j] == 0:
				cost = costMatrix[i+1, j]
			if matrix[i, j+1] == 0:
				cost += costMatrix[i, j+1]
			costMatrix[i, j] = cost
	return costMatrix

def main():

	#if you want result of the above matrix, use the following:
	#resultMatrix = numOfPaths(setUpMatrix(), setUpCostMatrix())
	print numOfPaths(setUpMatrix(), setUpCostMatrix())

if __name__ == '__main__':
	main()