n = int(input())
arr = [list(map(int, input().split()))
        for _ in range(n)]

def get_num_of_coin(row_s, row_e, col_s, col_e):
    num_of_coin = 0
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num_of_coin += arr[row][col]

    return num_of_coin

max_num_of_coin = 0

for row in range(n):
    for col in range(n):
        if row+2 >= n or col+2 >= n:
            continue
        num_of_coin = get_num_of_coin(row, row+2, col, col+2)

        max_num_of_coin = max(max_num_of_coin, num_of_coin)
print(max_num_of_coin)