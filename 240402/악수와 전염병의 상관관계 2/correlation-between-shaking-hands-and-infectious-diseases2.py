N, K, P, T = map(int, input().split())

# 전염 상태와 전염 가능한 악수 횟수를 기록
infected = {P: K}
transmission_count = {i: 0 for i in range(1, N+1)}  # 각 개발자별 전파 횟수 기록

handshakes = []
for _ in range(T):
    t, x, y = map(int, input().split())
    handshakes.append((t, x, y))

handshakes.sort()  # 악수 정보를 시간 순으로 정렬

for _, x, y in handshakes:
    # 감염 상태 업데이트
    if x in infected and infected[x] > 0:
        infected[y] = K
    if y in infected and infected[y] > 0:
        infected[x] = K
    
    # 악수를 통한 전파 횟수 업데이트
    if x in infected:
        transmission_count[x] += 1
        if transmission_count[x] >= K:
            infected[x] = 0  # 더 이상 전파할 수 없음
    if y in infected:
        transmission_count[y] += 1
        if transmission_count[y] >= K:
            infected[y] = 0  # 더 이상 전파할 수 없음

# 최종 감염 상태 출력
for i in range(1, N + 1):
    if i in infected:
        print(1, end="")
    else:
        print(0, end="")