n = int(input())
offset = 100
points = []
grid = [[0]*200 for _ in range(200)]

for _ in range(n):
    x1, y1 = map(int, input().split())
    points.append((x1, y1))

for x1, y1 in points:
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            grid[i+offset][j+offset] = 1

total_area = sum(row.count(1) for row in grid)
print(total_area)