inputData = input().split()
n = int(inputData[0])
k = int(inputData[1])

blockValues = list(map(int, input().split()))

if n <= 1 or k % n == 0:
    for val in blockValues:
        print(val, end=" ")
    print()
else:
    k = k % n

    headBlock = None
    tailBlock = None

    for val in blockValues:
        node = {"data": val, "next": None, "prev": None}
        if headBlock is None:
            headBlock = node
            tailBlock = node
        else:
            if tailBlock is not None:
                tailBlock["next"] = node
                node["prev"] = tailBlock
            tailBlock = node

    if headBlock is not None and tailBlock is not None:
        tailBlock["next"] = headBlock
        headBlock["prev"] = tailBlock

    stepsToNewTail = n - k
    currentBlock = headBlock

    for i in range(stepsToNewTail - 1):
        if currentBlock is None:
            break
        currentBlock = currentBlock.get("next")

    if currentBlock is None:
        currentBlock = headBlock

    newTailBlock = currentBlock
    newHeadBlock = currentBlock["next"] if currentBlock is not None else None

    if newTailBlock is not None:
        newTailBlock["next"] = None
    if newHeadBlock is not None:
        newHeadBlock["prev"] = None

    printCursor = newHeadBlock
    while printCursor != None:
        print(printCursor["data"], end=" ")
        printCursor = printCursor["next"]
    print()