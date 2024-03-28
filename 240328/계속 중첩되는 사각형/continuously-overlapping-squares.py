n = int(input())
offset = 100
grid = [[0]*200 for _ in range(200)]

for k in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if k % 2 == 0:
                grid[i+offset][j+offset] = 1
            else:
                grid[i+offset][j+offset] = 2

total_area = sum(row.count(2) for row in grid)
print(total_area)