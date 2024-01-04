sum = 0
grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

for i in range(4):
    for j in range(4):
        sum += grid[i][j]
        if j == i:
            break
print(sum)