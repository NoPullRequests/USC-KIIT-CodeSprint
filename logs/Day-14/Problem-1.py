n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
best = 0

while left < right:
    width = right - left
    height = min(arr[left], arr[right])
    
    score = height * width
    
    if score > best:
        best = score
        
    if arr[left] < arr[right]:
        left = left + 1
    else:
        right = right - 1

print(best)
