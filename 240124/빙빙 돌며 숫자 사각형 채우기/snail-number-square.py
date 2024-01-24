dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
x, y = 0, 0
dir_num = 0
arr[0][0] = 1
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n*m + 1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir_num = (dir_num+1) % 4
        x += dx[dir_num]
        y += dy[dir_num]

    arr[x][y] = i

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()