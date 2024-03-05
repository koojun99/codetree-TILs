stringA = input()
stringB = input()
n = 0
found = False  # 문자열이 일치하는지 여부를 추적하는 플래그

for _ in range(len(stringA)):  # 최대 stringA의 길이만큼만 회전
    stringA = stringA[-1] + stringA[:-1]
    n += 1
    if stringA == stringB:
        print(n)
        found = True
        break

if not found:  # 일치하는 문자열을 찾지 못한 경우
    print(-1)