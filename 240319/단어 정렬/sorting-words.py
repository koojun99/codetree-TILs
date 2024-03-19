words = []
n = int(input())
for _ in range(n):
    words.append(input())

words.sort()
for word in  words:
    print(word)