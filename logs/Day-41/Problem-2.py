import sys
from collections import deque

def main():
    d = list(map(int, sys.stdin.read().split()))
    if not d or d[1] == -1: return
    arr = d[1:d[0]+1]
    
    # 1. Map child-to-parent and find leaf indices using array indices
    n = len(arr)
    left, right = [-1]*n, [-1]*n
    is_leaf = [True]*n
    
    q, i = deque([0]), 1
    while q and i < n:
        curr = q.popleft()
        if i < n and arr[i] != -1:
            left[curr] = i; q.append(i); is_leaf[curr] = False
        i += 1
        if i < n and arr[i] != -1:
            right[curr] = i; q.append(i); is_leaf[curr] = False
        i += 1

    lb, lvs, rb = [], [], []

    # 2. Extract boundaries directly from index relations
    c = left[0]
    while c != -1 and not is_leaf[c]:
        lb.append(arr[c]); c = left[c] if left[c] != -1 else right[c]
        
    stk = [0]
    while stk:
        c = stk.pop()
        if is_leaf[c]: lvs.append(arr[c])
        else:
            if right[c] != -1: stk.append(right[c])
            if left[c] != -1: stk.append(left[c])
            
    c = right[0]
    while c != -1 and not is_leaf[c]:
        rb.append(arr[c]); c = right[c] if right[c] != -1 else left[c]

    # 3. Fast print output
    print(arr[0] if is_leaf[0] else " ".join(map(str, [arr[0]] + lb + lvs + rb[::-1])))

if __name__ == '__main__':
    main()