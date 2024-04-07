dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'E': 0,
    'S': 1,
    'N': 2,
    'W': 3
}

n = int(input())
x, y = 0, 0
total_time = 0
returned = False
moves = []

for _ in range(n):
    direction, dist = input().split()
    dist = int(dist)
    moves.append((direction, dist))

for direction, dist in moves:
    move_dir = mapper[direction]
    for _ in range(dist):
        if returned:  # 이미 돌아온 경우 더 이상 이동 처리하지 않음
            break
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny
        total_time += 1  # 이동할 때마다 시간 증가
        if nx == 0 and ny == 0:
            returned = True
            break

if not returned:
    total_time = -1
print(total_time)