n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(int, input().split())) for _ in range(m)]

# 상하좌우 이동을 위한 dx, dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_next(r, c):
    max_value = -1
    next_pos = (r, c)
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > max_value:
            max_value = grid[nx][ny]
            next_pos = (nx, ny)
    return next_pos

for _ in range(t):
    temp_grid = [[0 for _ in range(n)] for _ in range(n)]
    for r, c in marbles:
        nr, nc = find_next(r - 1, c - 1)
        temp_grid[nr][nc] += 1

    marbles = []
    for r in range(n):
        for c in range(n):
            # 겹치는 구슬이 없는 경우만 남김
            if temp_grid[r][c] == 1:
                marbles.append((r + 1, c + 1)) # 위치를 1-indexed로 조정

print(len(marbles))