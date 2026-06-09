n = int(input())
temps = list(map(int, input().split()))
queries = int(input())

for i in range(queries):
    line = input().split()
    left = int(line[0])
    right = int(line[1])
    
    subrange = temps[left : right + 1]
    
    highest = max(subrange)
    lowest = min(subrange)
    
    print(highest - lowest)