s = input().strip()

stack = []
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
is_valid = True

for char in s:
    if char in "([{<":
        stack.append(char)
    elif char in ")]}>":
        if not stack or stack[-1] != pairs[char]:
            is_valid = False
            break
        stack.pop()

if is_valid and not stack:
    print("VALID")
else:
    print("INVALID")