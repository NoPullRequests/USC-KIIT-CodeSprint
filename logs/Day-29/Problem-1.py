expression = input().strip()

stack = []
current_number = 0
last_operator = "+"

for i in range(len(expression)):
    char = expression[i]
    
    if char.isdigit():
        current_number = current_number * 10 + int(char)
        
    if char in "+-*/" or i == len(expression) - 1:
        if last_operator == "+":
            stack.append(current_number)
        elif last_operator == "-":
            stack.append(-current_number)
        elif last_operator == "*":
            stack.append(stack.pop() * current_number)
        elif last_operator == "/":
            top_number = stack.pop()
            stack.append(int(top_number / current_number))
            
        last_operator = char
        current_number = 0

print(sum(stack))