n = int(input())

for i in range(n):
    for j in range(1, i + 2):
        print(j, end="")
        
    k = (n * 2) - 2 * (i + 1)
    
    for j in range(k):
        print("@", end="")
        
    for j in range(i + 1, 0, -1):
        print(j, end="")
        
    print()
