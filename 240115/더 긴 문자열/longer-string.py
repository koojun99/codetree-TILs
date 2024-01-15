stringA, stringB = input().split()
if len(stringA) > len(stringB):
    print(stringA, end= " ")
    print(len(stringA))
elif len(stringB) > len(stringA):
    print(stringB, end=" ")
    print(len(stringB))
else:
    print("same")