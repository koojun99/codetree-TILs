binary = list(input())
decimal = 0

for i in range(len(binary)):
    decimal = decimal*2 + int(binary[i])

decimal *= 17
result = []
while True:
    if decimal < 2:
        result.append(decimal)
        break
    result.append(decimal%2)

    decimal //= 2

answer = result[::-1]

for elem in answer:
    print(elem, end="")