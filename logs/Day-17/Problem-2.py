n = int(input())
tokens = list(map(int, input().split()))
k = int(input())

head = None
tail = None

for value in tokens:
    node = {"data": value, "next": None}
    if tail is None:
        head = node
        tail = node
    else:
        tail["next"] = node
        tail = node

fast = head
slow = head

for i in range(k):
    if fast is None:
        break
    fast = fast["next"]

if fast is None:
    if head is not None:
        head = head["next"]
else:
    while fast["next"] is not None:
        fast = fast["next"]
        if slow is not None:
            slow = slow["next"]
    
    if slow is not None and slow["next"] is not None:
        slow["next"] = slow["next"]["next"]

curr = head
while curr != None:
    print(curr["data"], end=" ")
    curr = curr["next"]
print()
