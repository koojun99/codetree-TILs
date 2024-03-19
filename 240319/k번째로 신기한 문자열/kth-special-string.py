n, k, t = input().split()
n = int(n)
k = int(k)
size = len(t)
words = []
answer = []
for _ in range(n):
    words.append(input())

words.sort()

for word in words:
    if t == word[:size]:
        answer.append(word)

print(answer[k-1])