import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    scores = [int(x) for x in data[2:]]
    
    scores.sort()
    
    ans = 0
    total = 0
    
    i = 0
    while i < n:
        j = i
        while j < n and scores[j] == scores[i]:
            j += 1
            
        if total >= k:
            ans += (j - i)
            
        total += scores[i] * (j - i)
        i = j
        
    print(ans)

if __name__ == '__main__':
    main()
