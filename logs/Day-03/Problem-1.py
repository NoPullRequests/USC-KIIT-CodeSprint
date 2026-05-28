n = int(input())
arr = list(map(int, input().split()))

flag = 0 

for i in range(1, n):
    if arr[i] == arr[i - 1]:
        print("INVALID", i)
        flag = 1
        break

if flag == 0:
    print("VALID")
