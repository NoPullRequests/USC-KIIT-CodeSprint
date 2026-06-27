import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    m, n = int(data[0]), int(data[1])
    
    # Create empty buckets for each diagonal line
    diagonals = [[] for _ in range(m + n - 1)]
    
    # Read matrix data and group elements by their (row + col) sum
    idx = 2
    for r in range(m):
        for c in range(n):
            diagonals[r + c].append(int(data[idx]))
            idx += 1
            
    ans = []
    for i in range(len(diagonals)):
        # Even diagonals go up (so we reverse them)
        if i % 2 == 0:
            ans.extend(diagonals[i][::-1])
        # Odd diagonals go down (keep original order)
        else:
            ans.extend(diagonals[i])
                
    print(*(ans))

if __name__ == '__main__':
    main()