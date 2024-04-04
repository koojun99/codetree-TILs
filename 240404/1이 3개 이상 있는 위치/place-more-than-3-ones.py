def isValid(x, y, n):
    return 0 <= x < n and 0 <= y < n

n = int(input())
count = 0

dxs = [0, 1, 0, -1]
dys = [1, 0 , -1, 0]
grid = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        x, y = i, j
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if isValid(nx, ny, n) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            count += 1

print(count)