import sys

def main():
   
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    N = int(input_data[idx])
    M = int(input_data[idx+1])
    idx += 2
    
    
    INF = float('inf')
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    
    
    for i in range(1, N + 1):
        dist[i][i] = 0
        
 
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        
        if w < dist[u][v]:
            dist[u][v] = w
            
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
   
    Q = int(input_data[idx])
    idx += 1
    
    output = []
    for _ in range(Q):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        
        ans = dist[a][b]
        if ans == INF:
            output.append("-1")
        else:
            output.append(str(ans))
            
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()