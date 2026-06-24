import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    # Store all unique numbers in a Hash Set for O(1) lookups
    num_set = set()
    for i in range(1, n + 1):
        num_set.add(int(data[i]))
        
    longest_streak = 0
    
    for num in num_set:
        # Check if this number is the start of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # Count how long the sequence goes on
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            if current_streak > longest_streak:
                longest_streak = current_streak
                
    print(longest_streak)

if __name__ == '__main__':
    main()