temp = [list(map(int, input().split())) for _ in range(2)]
row_avg = []
col_avg = []
row_sum = 0
col_sum = 0
total_sum = 0
for i in range(2):
    for j in range(4):
        row_sum += temp[i][j]
    row_avg.append(row_sum/4.0)
    row_sum = 0

for j in range(4):
    for i in range(2):
        col_sum += temp[i][j]
    col_avg.append(col_sum/2.0)
    col_sum = 0

for i in range(2):
    for j in range(4):
        total_sum += temp[i][j]

# 행 평균 출력
for num in row_avg:
    print(num, end=' ')
print()

# 열 평균 출력
for num in col_avg:
    print(num, end=' ')
print()

# 전체 평균 출력
print(total_sum / 8.0)