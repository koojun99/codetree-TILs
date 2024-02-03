def max_path_sum(matrix, N):
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = matrix[0][0]

    # 첫 번째 행과 열 초기화
    for i in range(1, N):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    # 나머지 위치에 대해 최대 합 계산
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    return dp[N-1][N-1]

# 입력
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 출력
print(max_path_sum(matrix, N))