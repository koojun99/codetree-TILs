dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]


x, y = 0, 0
total_time = 0
returned = False
moves = []
commands = list(input())
move_dir = 2

for command in commands:
    if returned:
        break
        
    if command == "L":
        move_dir = (move_dir-1) % 4
    elif command == "R":
        move_dir = (move_dir+1) % 4
    else:
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if (nx, ny) == (0, 0):
            returned = True
        x, y = nx, ny
    total_time += 1

if not returned:
    total_time = -1
print(total_time)