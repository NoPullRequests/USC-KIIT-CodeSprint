total = int(input())

places = []
while len(places) < total:
    line = input().strip()
    if line:
        places.append(line)

pattern = ""
while not pattern:
    pattern = input().strip()

for i in range(total):
    for j in range(0, total - i - 1):
        if places[j] > places[j + 1]:
            temp = places[j]
            places[j] = places[j + 1]
            places[j + 1] = temp

found = False
patternsize = len(pattern)

for name in places:
    if len(name) >= patternsize:
        match = True
        for k in range(patternsize):
            if name[k] != pattern[k]:
                match = False
                break
        
        if match == True:
            print(name)
            found = True

if found == False:
    print(-1)
