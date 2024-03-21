class Resident:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
    
n = int(input())
residents = []
for _ in range(n):
    name, address, region = tuple(input().split())
    resident = Resident(name, address, region)
    residents.append(resident)
residents.sort(key = lambda x: x.name)
answer = residents[-1]

print("name " + answer.name)
print("addr " + answer.address)
print("city " + answer.region)