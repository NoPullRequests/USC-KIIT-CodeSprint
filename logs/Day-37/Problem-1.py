import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    
    # Using a min-heap to keep track of the K largest elements
    min_heap = []
    
    for i in range(2, n + 2):
        priority = int(data[i])
        
        if len(min_heap) < k:
            heapq.heappush(min_heap, priority)
        else:
            if priority > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, priority)
                
    # Extract elements from heap; they will naturally be in increasing order
    ans = []
    while min_heap:
        ans.append(heapq.heappop(min_heap))
        
    for i in range(len(ans)):
        if i == len(ans) - 1:
            print(str(ans[i]))
        else:
            print(str(ans[i]), end=" ")

if __name__ == '__main__':
    main()