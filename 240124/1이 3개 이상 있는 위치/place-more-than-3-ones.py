n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(n):
    for j in range(n):
        count = 0
        for dir_num in range(4):
            nx = i + dx[dir_num]
            ny = j + dy[dir_num]

            if in_range(nx, ny) and arr[nx][ny] == 1:
                count += 1

        if count >= 3:
            answer += 1

print(answer)