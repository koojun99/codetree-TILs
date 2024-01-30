n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 블록이 떨어질 수 있는 가장 낮은 위치 찾기
lowest_row = n
for col in range(k - 1, k + m - 1):
    for row in range(n):
        if grid[row][col] == 1:
            lowest_row = min(lowest_row, row)
            break

# 블록 놓기
for col in range(k - 1, k + m - 1):
    if lowest_row > 0:  # 격자판 바닥에 닿지 않은 경우
        grid[lowest_row - 1][col] = 1

# 결과 출력
for row in grid:
    for elem in row:
        print(elem, end=" ")
    print()