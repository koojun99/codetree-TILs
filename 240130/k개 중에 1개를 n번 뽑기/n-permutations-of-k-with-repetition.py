k, n = map(int, input().split())

def generate_combinations(k, n, combination = [], pos = 0):
    if pos == n:
        print(' '.join(map(str, combination)))
        return
    for i in range(1, k + 1):
        generate_combinations(k, n, combination + [i], pos + 1)

generate_combinations(k, n)