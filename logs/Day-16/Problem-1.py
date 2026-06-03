jewels = input().strip()
stones = input().strip()

premiumCount = 0

for badge in stones:
    if badge in jewels:
        premiumCount = premiumCount + 1

print(premiumCount)