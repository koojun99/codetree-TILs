n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def isValid(x, y):
    return 0 <= x < n and 0 <= y < m

def isAvailable(x, y):
    if not isValid(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False
    else:
        return True

def dfs(x, y):
    dxs = [0, 1]
    dys = [1, 0]

    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if isAvailable(nx, ny):
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)