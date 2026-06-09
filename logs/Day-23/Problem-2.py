n = int(input())
arr = list(map(int, input().split()))
queries = int(input())

for i in range(queries):
    line = input().split()
    left = int(line[0])
    right = int(line[1])
    
    subrange = arr[left : right + 1]
    
    counts = {}
    for num in subrange:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    score = 0
    for freq in counts.values():
        score += freq * freq
        
    print(score)
