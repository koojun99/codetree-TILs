n = int(input())
nums = list(map(int, input().split()))
answer = sorted(nums)
reverse = list(reversed(answer))
for elem in answer:
    print(elem, end=" ")
print()

for elem in reverse:
    print(elem, end=" ")