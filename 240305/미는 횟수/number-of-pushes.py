stringA = input()
stringB = input()
n = 0

while stringA != stringB:
    if n == len(stringA)-1:
        print(-1)
        break
    stringA = stringA[-1] + stringA[:-1]
    n += 1

print(n)