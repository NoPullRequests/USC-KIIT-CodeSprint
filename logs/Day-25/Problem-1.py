n = int(input())
heights = list(map(int, input().split()))

ans = 0
left = 0
right = n - 1

while left < right:
    width = right - left
    
    if heights[left] < heights[right]:
        current = heights[left] * width
        left += 1
    else:
        current = heights[right] * width
        right -= 1
        
    if current > ans:
        ans = current

print(ans)