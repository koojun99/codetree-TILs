from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def isAvailable(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid [x][y] == 0:
        return False
    return True

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0 ,0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if isAvailable(nx, ny):
                push(nx, ny)

push(0, 0)
bfs()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)