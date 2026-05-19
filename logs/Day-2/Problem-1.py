N = int(input("enter no. of players:"))
arr = list(map(int,input("enter the scores:").split()))

total = 0
i = 0
while i<N:
    total = total+arr[i]
    i = i+1

average = total/N

ans = 0
for x in arr:
    if x>average:
        ans = ans+1

print(ans)