import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    # 1. Parse inputs
    N = int(input_data[0])
    Q = int(input_data[1])
    
    resources = [0] + [int(x) for x in input_data[2:N+2]]
    
    adj = [[] for _ in range(N + 1)]
    idx = N + 2
    for _ in range(N - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # 2. Flatten Tree using Euler Tour
    tin = [0] * (N + 1)
    tout = [0] * (N + 1)
    timer = 1
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = timer
        timer += 1
        for neighbor in adj[node]:
            if neighbor != parent:
                dfs(neighbor, node)
        tout[node] = timer - 1

    dfs(1, 0)
    
    # 3. Fenwick Tree (Binary Indexed Tree) Implementation
    bit = [0] * (N + 2)
    
    def update(i, delta):
        while i <= N + 1:
            bit[i] += delta
            i += i & (-i)
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    # Initialize BIT with initial values
    for i in range(1, N + 1):
        update(tin[i], resources[i])
        
    # 4. Process Queries
    out = []
    for _ in range(Q):
        type_op = int(input_data[idx])
        if type_op == 1:
            X = int(input_data[idx+1])
            V = int(input_data[idx+2])
            delta = V - resources[X]
            resources[X] = V
            update(tin[X], delta)
            idx += 3
        else:
            X = int(input_data[idx+1])
            # Total sum in range [tin[X], tout[X]]
            ans = query(tout[X]) - query(tin[X] - 1)
            out.append(str(ans))
            idx += 2
            
    print('\n'.join(out))

if __name__ == '__main__':
    main()