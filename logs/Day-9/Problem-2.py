total = int(input())

names = []
while len(names) < total:
    line = input().strip()
    if line:
        names.append(line)

pref = names[0]

for i in range(1, total):
    while not names[i].startswith(pref):
        pref = pref[:-1]
        if not pref:
            break

print(pref)
