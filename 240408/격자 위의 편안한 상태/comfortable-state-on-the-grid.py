dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
n, m = map(int, input().split())
grid = [[0]*n for _ in range(n)]

def isValid(x, y):
    return 0 <= x < n and 0 <= y < n

def isComfort(x, y):
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if isValid(nx, ny) and grid[nx][ny] == 1:
            count += 1
    if count == 3:
        return True
    else:
        return False

for _ in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1
    if isComfort(x-1, y-1):
        print(1)
    else:
        print(0)