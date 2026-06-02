total = int(input())

participants = []
while len(participants) < total:
    line = input().strip()
    if line:
        parts = line.split()
        name = parts[0]
        score = int(parts[1])
        participants.append([name, score])

for i in range(total):
    for j in range(0, total - i - 1):
        if participants[j][1] > participants[j + 1][1]:
            temp = participants[j]
            participants[j] = participants[j + 1]
            participants[j + 1] = temp

for i in range(total):
    print(participants[i][0], participants[i][1])

