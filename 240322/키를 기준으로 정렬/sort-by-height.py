class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
people = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append(Person(name, height, weight))

people.sort(key = lambda x: x.height)
for person in people:
    print(person.name, person.height, person.weight)