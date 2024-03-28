offset = 1000
squares = []
grid = [[0]*2000 for _ in range(2000)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append((x1,y1,x2,y2))

# A와 B 직사각형 영역에 1로 마킹
for square in squares:  # 첫 번째와 두 번째 직사각형에 대해서만
    x1, y1, x2, y2 = square
    for i in range(x1, x2):
        for j in range(y1, y2):
            if grid[i+offset][j+offset] == 1:
                grid[i+offset][j+offset] = 2
            else:
                grid[i+offset][j+offset] = 1


x1, y1, x2, y2 = squares[0]
new_x = []
new_y = []
for i in range(x1, x2):
        for j in range(y1, y2):
            if grid[i+offset][j+offset] == 1:
                new_x.append(i)
                new_y.append(j)
answer_x = max(new_x) - min(new_x) + 1
answer_y = max(new_y) - min(new_y) + 1
print(answer_x * answer_y)