def backtrack(index, n, current, result):
    if index == n:
        result.add(''.join(map(str, current)))
        return
    for num in range(1, 5):
        if index + num <= n:  # 현재 위치에서 num 만큼 연속 가능한지 확인
            backtrack(index + num, n, current + [num] * num, result)

def count_beautiful_numbers(n):
    result = set()
    backtrack(0, n, [], result)
    return len(result)

n = int(input())
print(count_beautiful_numbers(n))