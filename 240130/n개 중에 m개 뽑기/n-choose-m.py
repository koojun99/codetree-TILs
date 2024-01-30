def generate_combinations(N, M, start, current_combination):
    if M == 0:
        print(" ".join(map(str, current_combination)))
        return
    
    for i in range(start, N + 1):
        current_combination.append(i)
        generate_combinations(N, M - 1, i + 1, current_combination)
        current_combination.pop()

# 입력 처리
N, M = map(int, input().split())

current_combination = []
generate_combinations(N, M, 1, current_combination)