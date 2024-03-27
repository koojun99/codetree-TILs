n = int(input())
offset = 100
squares = []
grid = [[0]*200 for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append((x1,y1,x2,y2))

for x1,y1,x2,y2 in squares:
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i+offset][j+offset] = 1

total_area = sum(row.count(1) for row in grid)
print(total_area)