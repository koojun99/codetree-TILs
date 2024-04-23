n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def isValid(x, y):
    return 0 <= x < n and 0 <= y < m

def max1(x, y):
    result = 0
    a, b, c, d = 0, 0, 0, 0
    if isValid(x - 1, y) and isValid(x, y + 1):
        a = grid[x][y] + grid[x-1][y] + grid[x][y+1]
    if isValid(x + 1, y) and isValid(x, y + 1):
        b = grid[x][y] + grid[x+1][y] + grid[x][y+1]
    if isValid(x + 1, y) and isValid(x, y - 1):
        c = grid[x][y] + grid[x+1][y] + grid[x][y-1]
    if isValid(x - 1, y) and isValid(x, y - 1):
        d = grid[x][y] + grid[x-1][y] + grid[x][y-1]
    result = max(a, b, c, d)
    return result

def max2(x, y):
    result = 0
    a, b = 0, 0
    if isValid(x - 1, y) and isValid(x+1, y):
        a = grid[x][y] + grid[x-1][y] + grid[x+1][y]
    if isValid(x, y - 1) and isValid(x, y + 1):
        b = grid[x][y] + grid[x][y-1] + grid[x][y+1]
    result = max(a, b)
    return result

max_val = 0
for i in range(n):
    for j in range(m):
        result = max(max1(i, j), max2(i, j))
        max_val = max(max_val, result)

print(max_val)