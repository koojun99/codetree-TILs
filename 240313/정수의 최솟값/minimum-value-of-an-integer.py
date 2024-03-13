def find(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input().split())
print(find(a, b, c))