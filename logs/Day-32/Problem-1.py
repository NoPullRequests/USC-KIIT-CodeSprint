import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    st1 = []
    st2 = []
    
    for line in lines[1:]:
        parts = line.split()
        if not parts:
            continue
        
        op = parts[0]
        if op == "REGISTER":
            st1.append(parts[1])
        elif op == "NEXT":
            if not st2:
                while st1:
                    st2.append(st1.pop())
            print(st2.pop() if st2 else -1)

if __name__ == '__main__':
    main()
