import sys
import heapq

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # Build adjacency list: adj[u] stores tuples of (v, travel_time, expiry_time)
    adj = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        t = int(input_data[idx+2])
        e = int(input_data[idx+3])
        adj[u].append((v, t, e))
        idx += 4
        
    # Initialize distances array with infinity
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    # Min-Heap for Dijkstra: stores tuples of (current_time, city)
    pq = [(0, 1)]
    
    while pq:
        curr_time, u = heapq.heappop(pq)
        
        # If we found a shorter path to u already, skip processing
        if curr_time > dist[u]:
            continue
            
        # Explore neighbors
        for v, t, e in adj[u]:
            # Condition check: Can we use this road before it expires?
            if curr_time < e:
                next_time = curr_time + t
                # Standard relaxation
                if next_time < dist[v]:
                    dist[v] = next_time
                    heapq.heappush(pq, (next_time, v))
                    
    # Format the output as per specifications
    output = []
    for i in range(1, N + 1):
        if dist[i] == INF:
            output.append("-1")
        else:
            output.append(str(dist[i]))
            
    print(" ".join(output))

if __name__ == '__main__':
    main()