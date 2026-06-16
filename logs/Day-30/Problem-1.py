s = input().strip()

stack = []
output = []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

for char in s:
    if char.isalnum():
        output.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
            output.append(stack.pop())
        stack.append(char)

while stack:
    output.append(stack.pop())

print("".join(output))
