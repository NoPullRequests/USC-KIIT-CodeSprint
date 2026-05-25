gridsize = int(input())
matrix = []

for rowindex in range(gridsize):
    rowdata = list(map(int, input().split()))
    matrix.append(rowdata)

firstdiagonalsum = 0
seconddiagonalsum = 0

for position in range(gridsize):
    firstdiagonalsum = firstdiagonalsum + matrix[position][position]
    seconddiagonalsum = seconddiagonalsum + matrix[position][gridsize - 1 - position]

if firstdiagonalsum == seconddiagonalsum:
    print("YES")
else:
    print("NO")
