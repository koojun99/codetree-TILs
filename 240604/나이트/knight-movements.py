from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
q = deque()

step = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [-2, -2, -1, 1, 2, 2, 1, -1], [-1, 1, 2, 2, 1, -1, -2, -2]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny]:
                push(nx, ny, step[x][y] + 1)

push(r1-1, c1-1, 0)
bfs()

if visited[r2-1][c2-1] == True:
    print(step[r2-1][c2-1])
else:
    print(-1)