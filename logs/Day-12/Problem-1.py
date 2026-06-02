n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

closest_diff = float('inf')
num1 = 0
num2 = 0

while left < right:
    current_sum = arr[left] + arr[right]
    
    if abs(current_sum) < closest_diff:
        closest_diff = abs(current_sum)
        num1 = arr[left]
        num2 = arr[right]
        
    if current_sum < 0:
        left = left + 1
    elif current_sum > 0:
        right = right - 1
    else:
        break

print(num1, num2)

