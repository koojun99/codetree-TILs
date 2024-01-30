def generate_permutations(n, current_permutation):
    if len(current_permutation) == n:
        print(" ".join(map(str, current_permutation)))
        return

    for i in range(1, n + 1):
        if i not in current_permutation:
            current_permutation.append(i)
            generate_permutations(n, current_permutation)
            current_permutation.pop()

# 입력 처리
n = int(input())

current_permutation = []
generate_permutations(n, current_permutation)