import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 1. Build Adjacency List (0-indexed for bitmasking convenience)
    adj = [[] for _ in range(N)]
    idx = 2
    for _ in range(M):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # Target mask where all N bits are set to 1 (all villages visited)
    TARGET_MASK = (1 << N) - 1
    
    # Memoization cache: memo[(curr_node, mask)]
    memo = {}
    
    def dfs(u, mask):
        if mask == TARGET_MASK:
            return True
        
        state = (u, mask)
        if state in memo:
            return memo[state]
            
        for v in adj[u]:
            # If village v has not been visited yet
            if not (mask & (1 << v)):
                if dfs(v, mask | (1 << v)):
                    memo[state] = True
                    return True
                    
        memo[state] = False
        return False

    # 2. Try starting the mission from every possible village
    for start_node in range(N):
        if dfs(start_node, 1 << start_node):
            print("MISSION POSSIBLE")
            return
            
    print("MISSION FAILED")

if __name__ == '__main__':
    main()
