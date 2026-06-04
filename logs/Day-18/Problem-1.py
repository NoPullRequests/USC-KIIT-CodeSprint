numStops = int(input())
stopValues = list(map(int, input().split()))
loopPos = int(input())

headStop = None
tailStop = None
stopsList = []

for val in stopValues:
    node = {"data": val, "next": None}
    stopsList.append(node)

    if headStop is None:
        headStop = node
        tailStop = node
    else:
        assert tailStop is not None
        tailStop["next"] = node
        tailStop = node

if loopPos != -1 and tailStop != None:
    tailStop["next"] = stopsList[loopPos]

slowBus = headStop
fastBus = headStop
loopFound = False

while fastBus is not None and fastBus["next"] is not None and slowBus is not None:
    slowBus = slowBus["next"]
    fastBus = fastBus["next"]["next"]

    if slowBus == fastBus:
        loopFound = True
        break 

if loopFound == True:
    print("YES")
else:
    print("NO")
