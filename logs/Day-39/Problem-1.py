import sys

def main():
    data = sys.stdin.read().split()
    if not data: 
        return
    n = int(data[0])
    
    # Create the empty grid
    board = [['.'] * n for _ in range(n)]
    ans = []
    
    # Check if it's safe to place a Queen at row 'r' and column 'c'
    def safe(r, c):
        for i in range(r):
            # How many rows above us is this line?
            dist = r - i  
            
            # 1. Check straight up
            if board[i][c] == 'Q': 
                return False
                
            # 2. Check up-left diagonal (column goes left by 'dist')
            if c - dist >= 0 and board[i][c - dist] == 'Q': 
                return False
                
            # 3. Check up-right diagonal (column goes right by 'dist')
            if c + dist < n and board[i][c + dist] == 'Q': 
                return False
                
        return True

    # The recursive explorer
    def solve(r):
        if r == n:
            # We found a valid board! Flatten it into a list of strings
            for row in board:
                ans.append(''.join(row))
            return
            
        for c in range(n):
            if safe(r, c):
                board[r][c] = 'Q'  # Place Queen
                solve(r + 1)       # Try next row
                board[r][c] = '.'  # Remove Queen (Backtrack)

    solve(0)
    
    if not ans:
        print("-1")
    else:
        # Print each row configuration on a brand new line
        print('\n'.join(ans))

if __name__ == '__main__':
    main()
