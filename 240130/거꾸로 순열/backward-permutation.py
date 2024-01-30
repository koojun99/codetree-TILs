def generate_permutations(n, current_permutation):
    if len(current_permutation) == n:
        print(" ".join(map(str, current_permutation)))
        return

    for i in range(n, 0, -1):  # n부터 1까지 역순으로 순회
        if i not in current_permutation:
            current_permutation.append(i)
            generate_permutations(n, current_permutation)
            current_permutation.pop()

# 입력 처리
n = int(input())

current_permutation = []
generate_permutations(n, current_permutation)