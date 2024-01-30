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
    new_positions = {}
    for r, c in marbles:
        nr, nc = find_next(r - 1, c - 1)
        if (nr, nc) in new_positions:
            new_positions[(nr, nc)] = 0  # Remove marbles in the same position
        else:
            new_positions[(nr, nc)] = 1
    marbles = [pos for pos, count in new_positions.items() if count > 0]

print(len(marbles))