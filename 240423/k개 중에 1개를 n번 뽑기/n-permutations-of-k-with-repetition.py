k, n = map(int, input().split())
selected = []

def solution():
    for num in selected:
        print(num, end= " ")
    print()
def find(count):
    if count == n:
        solution()
        return
    for i in range(1, k+1):
        selected.append(i)
        find(count+1)
        selected.pop()
find(0)