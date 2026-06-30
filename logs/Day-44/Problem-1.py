import sys

def main():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    P = int(input_data[0])
    
    # Track degrees and build adjacency list for connectivity checks
    # Using dictionaries since colors are provided as strings
    adj = {}
    in_degree = {}
    out_degree = {}
    unique_colors = set()
    
    idx = 1
    for _ in range(P):
        u = input_data[idx]
        v = input_data[idx+1]
        idx += 2
        
        unique_colors.add(u)
        unique_colors.add(v)
        
        if u not in adj: adj[u] = []
        if v not in adj: adj[v] = []
        
        adj[u].append(v)
        out_degree[u] = out_degree.get(u, 0) + 1
        in_degree[v] = in_degree.get(v, 0) + 1

    # 1. Verify Degree Constraints
    start_nodes = 0
    end_nodes = 0
    possible = True
    start_node_candidate = None

    for color in unique_colors:
        out_d = out_degree.get(color, 0)
        in_d = in_degree.get(color, 0)
        
        if out_d - in_d == 1:
            start_nodes += 1
            start_node_candidate = color
        elif in_d - out_d == 1:
            end_nodes += 1
        elif out_d != in_d:
            possible = False
            break

    if not possible or not ( (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1) ):
        print("ASSEMBLY IMPOSSIBLE")
        return

    # If all nodes have equal in/out degrees, pick any node with outgoing edges to start the connectivity check
    if start_node_candidate is None:
        for color in unique_colors:
            if out_degree.get(color, 0) > 0:
                start_node_candidate = color
                break

    # 2. Verify Connectivity using BFS (treating the graph as undirected)
    # We build an undirected version of the graph explicitly for this check
    undirected_adj = {color: [] for color in unique_colors}
    for u in adj:
        for v in adj[u]:
            undirected_adj[u].append(v)
            undirected_adj[v].append(u)

    visited = set()
    queue = [start_node_candidate]
    visited.add(start_node_candidate)
    
    for curr in queue:
        for neighbor in undirected_adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # All vertices that have at least one ribbon associated with them must be visited
    for color in unique_colors:
        if (out_degree.get(color, 0) > 0 or in_degree.get(color, 0) > 0) and color not in visited:
            print("ASSEMBLY IMPOSSIBLE")
            return

    print("ASSEMBLY POSSIBLE")

if __name__ == '__main__':
    main()