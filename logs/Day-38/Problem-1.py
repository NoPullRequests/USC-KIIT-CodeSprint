import sys

def main():
    # Read the input digits string
    data = sys.stdin.read().split()
    if not data:
        return
    
    digits = data[0]
    
    # Phone keypad mapping from digits to letters
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    ans = []
    
    # Backtracking function to build combinations
    def backtrack(index, current_string):
        # Base case: if the current combination length matches the input length
        if index == len(digits):
            ans.append(current_string)
            return
        
        # Get the letters that the current digit maps to
        current_digit = digits[index]
        letters = mapping[current_digit]
        
        # Try each letter for the current digit position
        for letter in letters:
            backtrack(index + 1, current_string + letter)
            
    # Start the backtracking process from index 0 with an empty string
    backtrack(0, "")
    
    # Print the results separated by spaces
    for i in range(len(ans)):
        if i == len(ans) - 1:
            print(ans[i])
        else:
            print(ans[i], end=" ")

if __name__ == '__main__':
    main()
