n = int(input())
tokens = list(map(int, input().split()))
k = int(input())

head = None
tail = None

for value in tokens:
    node = {"data": value, "next": None}
    if head == None:
        head = node
        tail = node
    else:
        tail["next"] = node
        tail = node

fast = head
slow = head

for i in range(k):
    fast = fast["next"]

if fast == None:
    head = head["next"]
else:
    while fast["next"] != None:
        fast = fast["next"]
        slow = slow["next"]
    
    slow["next"] = slow["next"]["next"]

curr = head
while curr != None:
    print(curr["data"], end=" ")
    curr = curr["next"]
print()
