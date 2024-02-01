from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_valid(x, y, n, m, arr):
    return 0 <= x < n and 0 <= y < m and arr[x][y] == 1


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 상, 하, 좌, 우
queue = deque([(0, 0)])
arr[0][0] = 0 # 시작점 방문 처리
found_path = False

while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1: # 도착점에 도달
        found_path = True
        break
    

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, n, m, arr):
            queue.append((nx, ny))
            arr[nx][ny] = 0 # 방문 처리

if found_path:
    print(1)
else:
    print(0)