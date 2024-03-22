n = int(input())
people = []

for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append((name, int(height), int(weight)))

people.sort(key=lambda x: (x[1], -x[2]))

for person in people:
    print(f"{person[0]} {person[1]} {person[2]}")