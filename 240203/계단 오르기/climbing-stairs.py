def count_ways(n):
    # n이 1이면 올라갈 수 있는 방법이 없습니다.
    if n == 1:
        return 0

    # 초기 상태 설정
    dp = [0] * (n+1)
    dp[0] = 1  # 시작점
    
    # 2와 3계단의 초기값 설정
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 1

    # 동적 계획법을 이용한 계산
    for i in range(4, n+1):
        dp[i] = (dp[i-2] + dp[i-3]) % 10007

    return dp[n]

# 입력 예제
n = int(input())
print(count_ways(n))