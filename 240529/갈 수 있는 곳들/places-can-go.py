from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
count = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def isAvailable(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid [x][y] == 1:
        return False
    return True

def push(x, y):
    global count
    count += 1
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

for _ in range(k):
    x, y = map(int,input().split())
    if not visited[x-1][y-1]:
        push(x-1, y-1)
        bfs()

print(count)