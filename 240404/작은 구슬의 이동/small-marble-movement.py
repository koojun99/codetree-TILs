dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

n, t = map(int, input().split())
x, y, direction = input().split()
x, y = int(x) , int(y)
move_dir = mapper[direction]

def isValid(x, y):
    return 0 < x <= n and 0 < y <= n

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if isValid(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x, y)