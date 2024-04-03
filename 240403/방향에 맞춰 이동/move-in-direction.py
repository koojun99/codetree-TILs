dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
n = int(input())
x, y = 0, 0

for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    if direction == "E":
        nx, ny = x + dx[0] * distance, y + dy[0] * distance
    elif direction == "S":
        nx, ny = x + dx[1] * distance, y + dy[1] * distance
    elif direction == "W":
        nx, ny = x + dx[2] * distance, y + dy[2] * distance
    else:
        nx, ny = x + dx[3] * distance, y + dy[3] * distance
    x, y = nx, ny

print(x, y)