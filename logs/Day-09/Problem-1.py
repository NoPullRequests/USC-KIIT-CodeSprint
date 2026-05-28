size = int(input())
nums = list(map(int, input().split()))

ans = [0] * size

left = 0
right = size - 1
pos = size - 1

while left <= right:
    lsq = nums[left] * nums[left]
    rsq = nums[right] * nums[right]

    if lsq > rsq:
        ans[pos] = lsq
        left = left + 1
    else:
        ans[pos] = rsq
        right = right - 1

    pos = pos - 1

print(*(ans))
