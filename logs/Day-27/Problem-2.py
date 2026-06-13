line = input().split()
n = int(line[0])
m = int(line[1])

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

target = int(input())

low = 0
high = (n * m) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    
    row = mid // m
    col = mid % m
    
    if matrix[row][col] == target:
        found = True
        break
    elif matrix[row][col] < target:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("FOUND")
else:
    print("NOT FOUND")