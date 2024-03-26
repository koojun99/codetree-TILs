a, b = map(int, input().split())
num = list(input())
decimal = 0

for i in range(len(num)):
    decimal = decimal*a + int(num[i])

result = []

while True:
    if decimal < b:
        result.append(decimal)
        break

    result.append(decimal%b)
    decimal //= b

answer = result[::-1]
for elem in answer:
    print(elem, end="")