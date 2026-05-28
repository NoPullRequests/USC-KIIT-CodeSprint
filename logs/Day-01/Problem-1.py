arr = [1, 0, 4, 0, 5, 2, 0]
n = len(arr)

for i in range(n):
    if arr[i]==0:
        for j in range(i+1, n):
            if arr[j]!=0:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                break

for i in range(n):
    print(arr[i], end=" ")



