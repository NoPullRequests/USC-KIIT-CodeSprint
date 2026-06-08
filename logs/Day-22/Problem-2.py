n = int(input())
nums = list(map(int, input().split()))

def merge(left, right):
    res = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def divide(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    
    return merge(left, right)

ans = divide(nums)

for i in range(n):
    if i == n - 1:
        print(ans[i])
    else:
        print(ans[i], end=" ")