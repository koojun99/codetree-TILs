n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1  # 인덱스는 0부터 시작하므로 1을 뺌
c -= 1

# 폭탄 터트리기
bomb_size = grid[r][c]
for i in range(max(0, r - bomb_size + 1), min(n, r + bomb_size)):
    grid[i][c] = 0
for j in range(max(0, c - bomb_size + 1), min(n, c + bomb_size)):
    grid[r][j] = 0

# 중력 작용
for j in range(n):
    column = [grid[i][j] for i in range(n) if grid[i][j] != 0]
    column = [0] * (n - len(column)) + column
    for i in range(n):
        grid[i][j] = column[i]

for row in grid:
    print(' '.join(map(str, row)))