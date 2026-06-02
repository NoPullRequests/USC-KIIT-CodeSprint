n = int(input())
weights = list(map(int, input().split()))
weights.sort()

left = 0
right = n - 1
maxLoad = 0

while left < right:
    currentLoad = weights[left] + weights[right]
    
    if currentLoad > maxLoad:
        maxLoad = currentLoad

    left = left + 1
    right = right - 1

print(maxLoad)
