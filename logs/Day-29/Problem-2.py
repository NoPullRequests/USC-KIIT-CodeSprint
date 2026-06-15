caption = input().strip()

stack = []

for char in caption:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)

if not stack:
    print("EMPTY")
else:
    print("".join(stack))
