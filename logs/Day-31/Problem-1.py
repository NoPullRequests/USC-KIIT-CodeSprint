import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    s = []
    m_s = []
    
    for line in lines[1:]:
        parts = line.split()
        if not parts:
            continue
        
        op = parts[0]
        if op == "PUSH":
            x = int(parts[1])
            s.append(x)
            m_s.append(x if not m_s or x < m_s[-1] else m_s[-1])
        elif op == "POP" and s:
            s.pop()
            m_s.pop()
        elif op == "MIN":
            print(m_s[-1] if m_s else -1)

if __name__ == '__main__':
    solve()
