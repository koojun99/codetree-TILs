def lcm(a, b):
    # 두 수 중 큰 수를 초기 최소공배수 후보로 설정
    max_num = max(a, b)
    lcm = max_num
    
    # 최소공배수 후보가 두 수의 배수가 될 때까지 증가
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += max_num
        
    return lcm

a, b = map(int, input().split())
print(lcm(a, b))  # 최소공배수 출력