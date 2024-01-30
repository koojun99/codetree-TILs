n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r -= 1
c -= 1
# 상하좌우 이동을 위한 dx, dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 위치에서 상하좌우로 이동하며 큰 숫자 찾기
def find_next(r, c):
    current_value = grid[r][c]
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > current_value:
            return nx, ny
    return None

path = [grid[r][c]]
while True:
    next_pos = find_next(r, c)
    if next_pos is None:  # 더 이동할 수 없는 경우
        break
    r, c = next_pos
    path.append(grid[r][c])

for elem in path:
    print(elem, end=" ")