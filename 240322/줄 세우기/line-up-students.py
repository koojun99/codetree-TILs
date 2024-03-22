n = int(input())
students = []
for i in range(n):
    height, weight = tuple(input().split())
    num = i+1
    students.append((int(height), int(weight), num))

students.sort(key=lambda x: (-x[0], -x[1], x[2]))
for student in students:
    print(f"{student[0]} {student[1]} {student[2]}")