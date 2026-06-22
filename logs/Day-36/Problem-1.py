import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    scores = []
    for i in range(n):
        scores.append(int(data[1 + i]))
        
    scores.sort(reverse=True)
    
    q_index = 1 + n
    q = int(data[q_index])
    
    for k in range(q):
        target = int(data[q_index + 1 + k])
        
        low = 0
        high = n - 1
        found_index = -1
        
        while low <= high:
            mid = (low + high) // 2
            if scores[mid] == target:
                found_index = mid
                break
            elif scores[mid] < target:
                high = mid - 1
            else:
                low = mid + 1
                
        if found_index != -1:
            rank = found_index + 1
            print("Rank " + str(rank))
        else:
            print("No Rank")

if __name__ == '__main__':
    main()
