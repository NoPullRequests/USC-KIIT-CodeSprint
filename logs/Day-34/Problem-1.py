import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    m = int(data[1])
    
    grid = []
    idx = 2
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[idx]))
            idx += 1
        grid.append(row)
        
    queue = []
    fresh_count = 0
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1
                
    minutes_passed = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c, minutes = queue.pop(0)
        minutes_passed = minutes
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, minutes + 1))
                
    if fresh_count == 0:
        print(minutes_passed)
    else:
        print(-1)

if __name__ == '__main__':
    main()