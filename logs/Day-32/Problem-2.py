import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    
    k = int(lines[0].split()[0])
    q = []
    
    for line in lines[1:]:
        parts = line.split()
        if not parts: continue
        
        op = parts[0]
        if op == "ENQUEUE":
            if len(q) == k:
                print("FULL")
            else:
                q.append(parts[1])
        elif op == "DEQUEUE":
            if not q:
                print("EMPTY")
            else:
                q.pop(0)
        elif op == "FRONT":
            print(q[0] if q else -1)

if __name__ == '__main__':
    main()
