def max_xor_combination(arr, m):
    n = len(arr)
    max_xor = 0
    
    # 모든 가능한 조합을 생성하고 XOR 연산 수행
    for i in range(1 << n):
        if bin(i).count('1') == m:  # m개의 숫자를 선택하는 경우
            selected_numbers = [arr[j] for j in range(n) if (i & (1 << j)) != 0]
            current_xor = selected_numbers[0]
            for num in selected_numbers[1:]:
                current_xor ^= num
            max_xor = max(max_xor, current_xor)
    
    return max_xor

# 입력 처리
n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = max_xor_combination(arr, m)
print(result)