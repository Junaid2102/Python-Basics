graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F', 'G'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : []
}

visited = set()

def dfs(visited, graph, state):
    if state not in visited:
        print (state)
    else:
        visited.add(state)
    for next in graph[state]:
        dfs(visited, graph, next)

print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
