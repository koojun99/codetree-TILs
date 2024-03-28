offset = 1000
squares = []
grid = [[0]*2000 for _ in range(2000)]

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append((x1,y1,x2,y2))

# A와 B 직사각형 영역에 1로 마킹
for square in squares[:2]:  # 첫 번째와 두 번째 직사각형에 대해서만
    x1, y1, x2, y2 = square
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i+offset][j+offset] = 1

x1, y1, x2, y2 = squares[2]  # 세 번째 직사각형 정보
for i in range(x1, x2):
    for j in range(y1, y2):
        grid[i+offset][j+offset] = 2

total_area = sum(row.count(1) for row in grid)
print(total_area)