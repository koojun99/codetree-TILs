num, trans = map(int, input().split())
result = []

while True:
    if num < trans:
        result.append(num)
        break
    result.append(num%trans)
    num //= trans

answer = result[::-1]

for elem in answer:
    print(elem, end="")