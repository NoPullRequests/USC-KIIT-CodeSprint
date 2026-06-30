import sys
from collections import deque

def main():
    d = list(map(int, sys.stdin.read().split()))
    if not d or d[1] == -1: return
    
    # 1. Compact Tree Build
    nodes = [None if x == -1 else type('N', (), {'v':x, 'l':None, 'r':None})() for x in d[1:d[0]+1]]
    q, i = deque([nodes[0]]), 1
    while q and i < len(nodes):
        curr = q.popleft()
        if i < len(nodes) and nodes[i]: curr.l = nodes[i]; q.append(nodes[i])
        i += 1
        if i < len(nodes) and nodes[i]: curr.r = nodes[i]; q.append(nodes[i])
        i += 1

    # 2. Morris Traversal with 0 extra memory space
    curr, prev = nodes[0], None
    first = second = None
    
    while curr:
        if not curr.l:
            if prev and prev.v > curr.v:
                if not first: first = prev
                second = curr
            prev, curr = curr, curr.r
        else:
            p = curr.l
            while p.r and p.r != curr: p = p.r
            if not p.r:
                p.r, curr = curr, curr.l
            else:
                p.r = None
                if prev and prev.v > curr.v:
                    if not first: first = prev
                    second = curr
                prev, curr = curr, curr.r

    # 3. Swap values and format output
    if first and second: first.v, second.v = second.v, first.v
    print(*(x.v if x else -1 for x in nodes))

if __name__ == '__main__':
    main()
