n = int(input())
students = []

for i in range(n):
    height, weight = tuple(map(int, input().split()))
    num = i+1
    students.append((height, weight, num))

students.sort(key=lambda x: (x[0], -x[1]))
for student in students:
    print(f"{student[0]} {student[1]} {student[2]}")