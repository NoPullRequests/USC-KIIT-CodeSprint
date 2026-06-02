n = int(input())
arr = list(map(int, input().split()))
swaps = 0

for i in range(n):
    low = i

    for j in range(i + 1, n):
        if arr[j] < arr[low]:
            low = j

    if low != i:
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp
        swaps = swaps + 1

for num in arr:
    print(num, end=" ")
print()

print(swaps)