n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
maxCoin = 0
def isValid(x, y):
    return 0 <= x < n and 0 <= y < n

def coin(row_s, row_e, col_s, col_e):
    coin = 0
    for x in range(row_s, row_e):
        for y in range(col_s, col_e):
            if isValid(x, y):
                coin += grid[x][y]

    return coin

for i in range(n):
    for j in range(n):
        maxCoin = max(maxCoin, coin(i, i+3, j, j+3))

print(maxCoin)