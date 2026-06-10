line = input().split()
n = int(line[0])
w = int(line[1])

weights = list(map(int, input().split()))

ans = 0
total = 0
left = 0

for right in range(n):
    total += weights[right]
    
    while total > w:
        total -= weights[left]
        left += 1
        
    length = right - left + 1
    if length > ans:
        ans = length

print(ans)
