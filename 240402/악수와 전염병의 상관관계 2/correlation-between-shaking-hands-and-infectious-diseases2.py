n, k, p, t = map(int, input().split())
people = [0]*n
count = [0]*n
people[p-1] = 1
events = []

for _ in range(t):
    time, a, b = map(int, input().split())
    events.append((time, a, b))

events.sort()

for time, a, b in events:
    if people[a-1] == 1 or people[b-1] == 1:
        if people[a-1] == 1 and count[a-1] < k:
            people[b-1] = 1
            count[a-1] += 1
        if people[b-1] == 1 and count[b-1] < k:
            people[a-1] = 1
            count[b-1] += 1

for elem in people:
    print(elem, end="")