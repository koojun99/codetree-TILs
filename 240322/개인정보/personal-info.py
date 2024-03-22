people = []
for _ in range(5):
    name, height, weight = tuple(input().split())
    people.append((name, int(height), float(weight)))

people.sort(key=lambda x: x[0])
print("name")
for person in people:
    print(f"{person[0]} {person[1]} {person[2]}")
print()
people.sort(key=lambda x: -x[1])
print("height")
for person in people:
    print(f"{person[0]} {person[1]} {person[2]}")