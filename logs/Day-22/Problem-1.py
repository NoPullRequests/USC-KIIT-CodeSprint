n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

paths = []
seen = [[False] * n for i in range(n)]

def find(r, c, s):
    if r == n - 1 and c == n - 1:
        paths.append(s)
        return
    seen[r][c] = True

    if r + 1 < n and not seen[r + 1][c] and maze[r + 1][c] == 1:
        find(r + 1, c, s + "D")
    if c - 1 >= 0 and not seen[r][c - 1] and maze[r][c - 1] == 1:
        find(r, c - 1, s + "L")
    if c + 1 < n and not seen[r][c + 1] and maze[r][c + 1] == 1:
        find(r, c + 1, s + "R")
    if r - 1 >= 0 and not seen[r - 1][c] and maze[r - 1][c] == 1:
        find(r - 1, c, s + "U")
    seen[r][c] = False

if maze[0][0] == 1:
    find(0, 0, "")

if len(paths) == 0:
    print(-1)
else:
    paths.sort()
    for p in paths:
        print(p)