def min_path_sum(matrix, N):
    dp = [[0] * N for _ in range(N)]
    dp[0][N-1] = matrix[0][N-1]  # 시작점 초기화

    # 첫 번째 행 초기화
    for j in range(N-2, -1, -1):
        dp[0][j] = dp[0][j+1] + matrix[0][j]

    # 첫 번째 열 초기화
    for i in range(1, N):
        dp[i][N-1] = dp[i-1][N-1] + matrix[i][N-1]

    # 나머지 위치에 대해 최소 합 계산
    for i in range(1, N):
        for j in range(N-2, -1, -1):
            dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + matrix[i][j]

    return dp[N-1][0]

# 입력
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 출력
print(min_path_sum(matrix, N))