n = int(input())
userids = list(map(int, input().split()))
randoms = list(map(int, input().split()))

for i in range(n):
    print(userids[i], randoms[i])