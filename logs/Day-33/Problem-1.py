import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    passengers = []
    
    idx = 1
    for i in range(n):
        pid = int(input_data[idx])
        priority = int(input_data[idx+1])
        passengers.append((priority, i, pid))
        idx += 2
        
    passengers.sort(key=lambda x: (-x[0], x[1]))
    
    for p in passengers:
        print(p[2])

if __name__ == '__main__':
    main()