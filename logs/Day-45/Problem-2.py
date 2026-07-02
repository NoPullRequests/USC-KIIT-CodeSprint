import sys
from collections import deque

def main():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
   
    adj = [[] for _ in range(N + 1)]
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    
    assignment = [0] * (N + 1)
    
    
    for i in range(1, N + 1):
        if assignment[i] == 0:
            
            queue = deque([i])
            assignment[i] = 1 
            
            while queue:
                curr = queue.popleft()
                curr_pipeline = assignment[curr]
                
                next_pipeline = 2 if curr_pipeline == 1 else 1
                
                for neighbor in adj[curr]:
                    if assignment[neighbor] == 0:
                        # Assign opposite pipeline and add to queue
                        assignment[neighbor] = next_pipeline
                        queue.append(neighbor)
                    elif assignment[neighbor] == curr_pipeline:
              
                        print("NO")
                        return
                        
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    main()
