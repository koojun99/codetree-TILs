n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for x, y in edges:
    graph[x].append(y)
    graph[y].append(x)
dfs(graph, 1, visited)
print(sum(visited)-1)