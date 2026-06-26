import sys

# Increase the recursion limit for deep trees
sys.setrecursionlimit(300000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    treasure = [0] * (n + 1)
    for i in range(n):
        treasure[i + 1] = int(data[1 + i])
        
    adj = []
    for i in range(n + 1):
        adj.append([])
        
    idx = 1 + n
    for i in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    total_treasure = 0
    
    def dfs(node, parent, level):
        nonlocal total_treasure
        
        if level % 2 == 0:
            total_treasure += treasure[node]
            
        for neighbor in adj[node]:
            if neighbor != parent:
                dfs(neighbor, node, level + 1)
                
    dfs(1, 0, 0)
    
    print(total_treasure)

if __name__ == '__main__':
    main()
