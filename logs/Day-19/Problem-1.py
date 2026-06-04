n = int(input())
shelvesOne = list(map(int, input().split()))
m = int(input())
shelvesTwo = list(map(int, input().split()))
intersectValue = int(input())

nodesOne = []
headOne = None
tailOne = None

for val in shelvesOne:
    node = {"data": val, "next": None}
    nodesOne.append(node)
    if headOne == None:
        headOne = node
        tailOne = node
    else:
        # ensure tailOne is not None for static analyzers
        assert tailOne is not None
        tailOne["next"] = node
        tailOne = node

matchNode = None
if intersectValue != -1:
    for node in nodesOne:
        if node["data"] == intersectValue:
            matchNode = node
            break 

headTwo = None
tailTwo = None
intersectFound = None

for val in shelvesTwo:
    if matchNode != None and val == intersectValue:
        node = matchNode
        if intersectFound == None:
            intersectFound = node
    else:
        node = {"data": val, "next": None}

    if headTwo == None:
        headTwo = node
        tailTwo = node
    else:
        assert tailTwo is not None
        tailTwo["next"] = node
        tailTwo = node

if intersectFound != None:
    print(intersectFound["data"])
else:
    print("-1")
