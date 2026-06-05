n = int(input())
playerIds = list(map(int, input().split()))
k = int(input())

survivorIndex = 0
for i in range(2, n + 1):
    survivorIndex = (survivorIndex + k) % i

print(playerIds[survivorIndex])
