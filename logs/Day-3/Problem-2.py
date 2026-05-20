n = int(input())

for i in range(n):
    # This matches exactly how you did it on Day 2!
    character = chr(65 + i)
    
    for j in range(n):
        if j == i or j == (n - i - 1):
            print(character, end=" ")
        else:
            print("*", end=" ")
            
    print()