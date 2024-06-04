from collections import deque

n, m = map(int, input().split())
q = deque()
grid = [list(map(int, input().split())) for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
        return True
    return False

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny]:
                push(nx, ny, step[x][y] + 1)

push(0, 0, 0)
bfs()

if visited[n-1][m-1] == True:
    print(step[n-1][m-1])
else:
    print(-1)