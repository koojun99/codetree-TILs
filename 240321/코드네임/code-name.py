class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = tuple(input().split())
    score = int(score)
    agents.append(Agent(name, score))
agents.sort(key = lambda x: x.score)
agent = agents[0]

print(agent.name, agent.score)