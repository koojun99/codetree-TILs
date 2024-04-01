n, m, k = map(int, input().split())
students = [0]*n

found = False  # k까지 도달한 student가 있는지 추적하는 플래그

for _ in range(m):
    penalty = int(input())
    students[penalty-1] += 1
    if k in students:
        print(students.index(k) + 1)
        found = True  # k까지 도달한 student를 찾음
        break

if not found:  # 반복문을 다 돌고도 k까지 도달한 student를 못 찾았다면
    print(-1)