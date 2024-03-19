n, k, t = input().split()
n = int(n)
k = int(k)
words = []
answer = []
for _ in range(n):
    words.append(input())

words.sort()

for word in words:
    if t in word:
        answer.append(word)

print(answer[k-1])