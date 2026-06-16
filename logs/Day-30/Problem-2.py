s = input().strip()

stack = []

for i in range(len(s) - 1, -1, -1):
    char = s[i]
    
    if char.isdigit():
        stack.append(int(char))
    else:
        operand1 = stack.pop()
        operand2 = stack.pop()
        
        if char == '+':
            stack.append(operand1 + operand2)
        elif char == '-':
            stack.append(operand1 - operand2)
        elif char == '*':
            stack.append(operand1 * operand2)
        elif char == '/':
            stack.append(int(operand1 / operand2))

print(stack[0])