from collections import deque
import sys

# Fast I/O
input = sys.stdin.read

def solve():
    lines = input().splitlines()
    if not lines:
        return
        
    q = int(lines[0])
    queue = deque()
    
    for i in range(1, q + 1):
        command = lines[i].split()
        
        if command[0] == "REGISTER":
            student_id = command[1]
            queue.append(student_id)
            
        elif command[0] == "WITHDRAW":
            if queue:
                queue.popleft()
            else:
                print(-1)
                
        elif command[0] == "NEXT":
            if queue:
                print(queue.popleft())
            else:
                print(-1)

solve()