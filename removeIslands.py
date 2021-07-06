"""
Difficulty: Medium


  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s. The matrix
  represents a two-toned image, where each 1 represents black and
  each 0 represents white. An island is defined as any number of
  1s that are horizontally or vertically adjacent (but not
  diagonally adjacent) and that don't touch the border of the image. In other
  words, a group of horizontally or vertically adjacent 1s isn't an
  island if any of those 1s are in the first row, last row, first
  column, or last column of the input matrix.

  Note that an island can twist. In other words, it doesn't have to be a
  straight vertical line or a straight horizontal line; it can be L-shaped, for
  example.

  You can think of islands as patches of black that don't touch the border of
  the two-toned image.

  Write a function that returns a modified version of the input matrix, where
  all of the islands are removed. You remove an island by replacing it with
  0s.
  Naturally, you're allowed to mutate the input matrix.

  Sample input:
    matrix  =
    [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
    ]

    Sample output:
    =[
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    ]

    // The islands that were removed can be clearly seen here:
    [
    [ ,  ,  ,  ,  ,  ],
    [ , 1,  ,  ,  ,  ],
    [ ,  , 1,  ,  ,  ],
    [ ,  ,  ,  ,  ,  ],
    [ ,  , 1, 1,  ,  ],
    [ ,  ,  ,  ,  ,  ],
    ]
"""


# Solution 1
# O(nm) time and space where n is height of matrix and m is width of matrix
def removeIslands(matrix):
    visited = [[False for col in range(len(matrix[0]))]
               for row in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1):
                markAsVisited(visited, matrix, i, j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j] == False:
                matrix[i][j] = 0
    return matrix


def markAsVisited(visited, matrix, row, col):
    if matrix[row][col] == 1 and visited[row][col] == False:

        visited[row][col] = True

    if row - 1 >= 0 and matrix[row-1][col] == 1 and visited[row-1][col] == False:
        markAsVisited(visited, matrix, row-1, col)
    if row + 1 < len(matrix) and matrix[row+1][col] == 1 and visited[row+1][col] == False:
        markAsVisited(visited, matrix, row+1, col)
    if col - 1 >= 0 and matrix[row][col-1] == 1 and visited[row][col-1] == False:
        markAsVisited(visited, matrix, row, col-1)
    if col + 1 < len(matrix[0]) and matrix[row][col+1] == 1 and visited[row][col+1] == False:
        markAsVisited(visited, matrix, row, col+1)





# Solution 2
# O(nm) time and space where n is height of matrix and m is width of matrix
def removeIslands(matrix):
    
	# first column, j = 0
	for i in range(len(matrix)):
		if matrix[i][0] == 1:
			changeToTwo(matrix, i, 0)
	# last column, j = len(matrix[0])-1
	for i in range(len(matrix)):
		if matrix[i][len(matrix[0])-1] == 1:
			changeToTwo(matrix, i, len(matrix[0])-1)
			
	# first row, i = 0
	for j in range(len(matrix[0])):
		if matrix[0][j] == 1:
			changeToTwo(matrix, 0, j)
			
	# last row, i = len(matrix) -1 
	for j in range(len(matrix[0])):
		if matrix[len(matrix)-1][j] == 1:
			changeToTwo(matrix, len(matrix)-1, j)
			
	# change the remaining 1s to 0s
	for i in range(1, len(matrix)-1):
		for j in range(1, len(matrix[0])-1):
			if matrix[i][j] == 1:
				matrix[i][j] = 0
	
	# change 2s back to 1s
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 2:
				matrix[i][j] = 1
		
	return matrix


def changeToTwo(matrix, row, col):
	
	if matrix[row][col] == 1:
		matrix[row][col] = 2
		
	if row - 1 >= 0 and matrix[row-1][col] == 1:
		changeToTwo(matrix, row-1, col)
	if row + 1 < len(matrix) and matrix[row+1][col] == 1:
		changeToTwo(matrix, row+1, col)
	if col - 1 >= 0 and matrix[row][col-1] == 1:
		changeToTwo(matrix, row, col-1)
	if col + 1 < len(matrix[0]) and matrix[row][col+1] == 1:
		changeToTwo(matrix, row, col+1)
			