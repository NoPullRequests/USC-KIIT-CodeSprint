gridsize = int(input())

matrix = []
for i in range(gridsize):
    line = input().strip().replace(" ", "")
    rowdata = [int(character) for character in line]
    matrix.append(rowdata)

resultgrid = [["S" for blank in range(gridsize)] for blank in range(gridsize)]

for row in range(gridsize):
    for column in range(gridsize):
        if matrix[row][column] == 1:
            resultgrid[row][column] = "O"
            
            if row - 1 >= 0 and matrix[row - 1][column] == 0:
                resultgrid[row - 1][column] = "X"
                
            if row + 1 < gridsize and matrix[row + 1][column] == 0:
                resultgrid[row + 1][column] = "X"
                
            if column - 1 >= 0 and matrix[row][column - 1] == 0:
                resultgrid[row][column - 1] = "X"
                
            if column + 1 < gridsize and matrix[row][column + 1] == 0:
                resultgrid[row][column + 1] = "X"

for printrow in resultgrid:
    print(" ".join(printrow))