n, m = map(int, input().split())
grid = []

# 격자 정보 입력
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 행복한 수열을 체크하는 함수
def count_happy_sequences(arr, m):
    if m == 1:
        return 1 if arr else 0  # m이 1인 경우, 수열에 숫자가 있으면 행복한 수열로 간주

    count = 0
    consecutive = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            consecutive += 1
            if consecutive >= m and count == 0:  # 첫 번째로 m개 이상 연속되는 경우에만 count를 1로 설정
                count = 1
        else:
            consecutive = 1

    return count

# 각 행을 검사하여 행복한 수열 개수를 세기
happy_row_count = 0
for row in grid:
    happy_row_count += count_happy_sequences(row,m)

# 각 열을 검사하여 행복한 수열 개수를 세기
happy_col_count = 0
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    happy_col_count += count_happy_sequences(col,m)

# 총 행복한 수열의 개수 출력
total_happy_sequences = happy_row_count + happy_col_count
print(total_happy_sequences)