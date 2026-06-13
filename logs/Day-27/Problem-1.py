n = int(input())
signals = list(map(int, input().split()))

low = 0
high = n - 1

while low < high:
    mid = (low + high) // 2
    if signals[mid] < signals[mid + 1]:
        low = mid + 1
    else:
        high = mid

print(signals[low])