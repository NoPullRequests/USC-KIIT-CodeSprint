N = int(input("enter the number of transaction:"))
amounts = list(map(int,input("enter amount:").split()))

unique = []
for i in range(N):
    found = 0
    for j in range(len(unique)):
        if amounts[i]==unique[j]:
            found = 1
            break
    if found==0:
        unique.append(amounts[i])

largest = unique[0]
for i in range(len(unique)):
    if unique[i]>largest:
        largest = unique[i]

second = unique[0]
for i in range(len(unique)):
    if unique[i]>second and unique[i]!=largest:
        second = unique[i]

print(second)
