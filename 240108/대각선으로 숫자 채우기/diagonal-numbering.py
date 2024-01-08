n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1
for d in range(2 * n - 1):  # 대각선의 총 개수
    for i in range(n):  # 행
        for j in range(n):  # 열
            if i + j == d:  # 대각선의 조건을 만족하면
                arr[i][j] = num
                num += 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()