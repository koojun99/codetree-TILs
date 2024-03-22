students = []
n = int(input())

for _ in range(n):
    name, a, b, c = tuple(input().split())
    students.append((name, int(a), int(b), int(c)))

students.sort(key=lambda x: x[1] + x[2] + x[3])
for student in students:
    name, a, b, c = student
    print(name, a, b, c)