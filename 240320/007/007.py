class Mission:
    def __init__(self, code, loc, time):
        self.code = code
        self.loc = loc
        self.time = time

code, location, time = input().split()
mission = Mission(code, location, time)

print("secret code : " + mission.code)
print("meeting point : " + mission.loc)
print("time : " + mission.time)