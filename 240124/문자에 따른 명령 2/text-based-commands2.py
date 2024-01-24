dir_num = 0 
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

command = input()

for i in range(len(command)):
    if command[i] == "L":
        dir_num = (dir_num-1)%4
    elif command[i] == "R":
        dir_num = (dir_num+1)%4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)