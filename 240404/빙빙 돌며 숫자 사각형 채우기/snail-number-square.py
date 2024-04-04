dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
answer = [[0]*m for _ in range(n)]
dir_num = 0
x, y = 0, 0
num = 1

def isValid(x, y):
    return 0 <= x < n and 0 <= y < m

answer[x][y] = 1
for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not isValid(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]  # 방향 전환 후의 새로운 위치 계산
    x, y = nx, ny
    answer[x][y] = i

for row in answer:
    for elem in row:
        print(elem, end = " ")
    print()