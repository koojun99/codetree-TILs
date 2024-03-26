num = int(input())
binary = []
while True:
    if num < 2:
        binary.append(num)
        break
    binary.append(num%2)
    num //= 2

answer = binary[::-1]

for elem in answer:
    print(elem, end="")