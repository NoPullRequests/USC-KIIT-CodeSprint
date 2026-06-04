n = int(input())
weights = list(map(int, input().split()))

head = None
tail = None

for value in weights:
    node = {"data": value, "next": None}
    if head == None:
        head = node
        tail = node
    else:
        if tail is not None:
            tail["next"] = node
        tail = node

prev = None
curr = head

while curr != None:
    nxt = curr["next"]
    curr["next"] = prev
    prev = curr
    curr = nxt

curr = prev
while curr != None:
    print(curr["data"], end=" ")
    curr = curr["next"]
print()