n = int(input())

moves = 0

def hanoi(plates, source, destination, auxiliary):
    global moves
    if plates == 1:
        print("Move plate 1 from " + source + " to " + destination)
        moves += 1
        return
        
    hanoi(plates - 1, source, auxiliary, destination)
    
    print("Move plate " + str(plates) + " from " + source + " to " + destination)
    moves += 1
    
    hanoi(plates - 1, auxiliary, destination, source)

hanoi(n, "A", "C", "B")
print("Total Moves =", moves)