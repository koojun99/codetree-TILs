dir_num = 3
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
command = input()

for char in command:
    if char == "L":
        dir_num = (dir_num - 1) % 4
    elif char == "R":
        dir_num = (dir_num + 1) % 4
    elif char == "F":
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        x, y = nx, ny

print(x, y)