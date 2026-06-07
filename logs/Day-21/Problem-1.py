lists = int(input())
merged = []

for i in range(lists):
    sublist = list(map(int, input().split()))
    merged.extend(sublist)

merged.sort()

for i in range(len(merged)):
    if i == len(merged) - 1:
        print(merged[i])
    else:
        print(merged[i], end=" ")