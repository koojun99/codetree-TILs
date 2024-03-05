stringA = input()
stringB = input()
n = 0

while stringA != stringB:
    stringA = stringA[-1] + stringA[:-1]
    n += 1

print(n)