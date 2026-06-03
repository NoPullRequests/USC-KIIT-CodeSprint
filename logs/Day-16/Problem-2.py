inputData = input().split()
n = int(inputData[0])
k = int(inputData[1])
x = int(inputData[2])

arr = list(map(int, input().split()))

foundStreak = False

for i in range(n - k + 1):
    currentSum = 0
    hasZero = False
    
    for j in range(i, i + k):
        currentSum = currentSum + arr[j]
        if arr[j] == 0:
            hasZero = True
            
    if currentSum >= x and hasZero == False:
        foundStreak = True

if foundStreak == True:
    print("YES")
else:
    print("NO")