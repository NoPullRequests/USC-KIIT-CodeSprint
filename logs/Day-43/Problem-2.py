import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    edges = []
    adj_forward = [[] for _ in range(N + 1)]
    adj_backward = [[] for _ in range(N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((u, v, w))
        adj_forward[u].append(v)
        adj_backward[v].append(u)
        idx += 3
        
    # 1. BFS from 1 to find all reachable nodes
    reachable_from_1 = [False] * (N + 1)
    reachable_from_1[1] = True
    queue = [1]
    for u in queue:
        for v in adj_forward[u]:
            if not reachable_from_1[v]:
                reachable_from_1[v] = True
                queue.append(v)
                
    # 2. BFS from N backwards to find all nodes that can reach N
    can_reach_N = [False] * (N + 1)
    can_reach_N[N] = True
    queue = [N]
    for v in queue:
        for u in adj_backward[v]:
            if not can_reach_N[u]:
                can_reach_N[u] = True
                queue.append(u)
                
    # If destination N is not reachable from 1, immediately stop
    if not reachable_from_1[N]:
        print("UNREACHABLE")
        return

    # 3. Bellman-Ford variant to maximize profit
    INF = float('inf')
    profit = [-INF] * (N + 1)
    profit[1] = 0
    
    # Relax edges N - 1 times
    for _ in range(N - 1):
        for u, v, w in edges:
            if profit[u] != -INF and profit[u] + w > profit[v]:
                profit[v] = profit[u] + w
                
    # 4. 1 more relaxation round to check for valid infinite profit cycles
    infinite_profit = False
    for u, v, w in edges:
        if profit[u] != -INF and profit[u] + w > profit[v]:
            # The cycle is only a problem if it can affect the path from 1 to N
            if reachable_from_1[u] and can_reach_N[v]:
                infinite_profit = True
                break
                
    if infinite_profit:
        print("INFINITE PROFIT")
    else:
        print(profit[N])

if __name__ == '__main__':
    main()