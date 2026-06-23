import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    k = int(data[1])
    
    # Store frequencies of prefix sums using a dictionary (Hash Map)
    prefix_map = {}
    prefix_map[0] = 1  # Base case: a prefix sum of 0 has occurred once
    
    current_sum = 0
    ans = 0
    
    for i in range(2, n + 2):
        num = int(data[i])
        current_sum += num
        
        # If (current_sum - k) exists in our map, it means we found 
        # subarrays that sum up to exactly k
        if (current_sum - k) in prefix_map:
            ans += prefix_map[current_sum - k]
            
        # Record the current prefix sum into our map
        if current_sum in prefix_map:
            prefix_map[current_sum] += 1
        else:
            prefix_map[current_sum] = 1
            
    print(ans)

if __name__ == '__main__':
    main()
