n, m = map(int, input().split())
A = [0]
B = [0]
hall_of_fame = [0]
count = 0
currentA = 0
currentB = 0

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        currentA += v
        A.append(currentA)

for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        currentB += v
        B.append(currentB)

length = len(A)

for i in range(1, length):
    if A[i] > B[i]:
        hall_of_fame.append("A")
    elif B[i] > A[i]:
        hall_of_fame.append("B")
    else:
        hall_of_fame.append("AB")

for i in range(1, length):
    if hall_of_fame[i] != hall_of_fame[i-1]:
        count += 1
print(count)