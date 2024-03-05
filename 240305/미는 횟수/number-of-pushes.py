stringA = input()
stringB = input()
n = 0

while stringA != stringB:
    if n == len(stringA):
        print(-1)
    stringA = stringA[-1] + stringA[:-1]
    n += 1

print(n)