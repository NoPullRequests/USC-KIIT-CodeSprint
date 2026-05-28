totalbracelets = int(input())
braceletids = list(map(int, input().split()))

scannertracker = 0

for identity in braceletids:
    scannertracker = scannertracker ^ identity

if scannertracker == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
