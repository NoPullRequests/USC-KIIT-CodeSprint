size = int(input())
nodes = input().split()

for i in range(size):
    if i == size - 1:
        print(nodes[i])
    else:
        print(nodes[i], end=" ")