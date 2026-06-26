import sys

sys.setrecursionlimit(300000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    root = None
    for i in range(n):
        score = int(data[1 + i])
        root = insert(root, score)
        
    k = int(data[1 + n])
    
    count = 0
    ans = -1
    
    def reverse_inorder(node):
        nonlocal count, ans
        if node is None or count >= k:
            return
            
        reverse_inorder(node.right)
        
        count += 1
        if count == k:
            ans = node.val
            return
            
        reverse_inorder(node.left)

    reverse_inorder(root)
    print(ans)

if __name__ == '__main__':
    main()