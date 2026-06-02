n, target = map(int, input().split())
arr = list(map(int, input().split()))

seen = {0: -1}
currentSum = 0
maxLen = 0

for i in range(n):
    currentSum = currentSum + arr[i]
    
    if (currentSum - target) in seen:
        length = i - seen[currentSum - target]
        if length > maxLen:
            maxLen = length
            
    if currentSum not in seen:
        seen[currentSum] = i

print(maxLen)