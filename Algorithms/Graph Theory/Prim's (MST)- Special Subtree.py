class node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

n,m = list(map(int, input().strip().split()))

# Build graph
graph = {}
for i in range(m):
    x,y,r = list(map(int, input().strip().split()))
    
    # Add the two nodes if they're not already in the graph
    if x not in graph:
        graph[x] = node(x)
    if y not in graph:
        graph[y] = node(y)
        
    # Connect the two nodes
    graph[x].connections[graph[y]] = r
    graph[y].connections[graph[x]] = r

# Add starting node to visited list
s = int(input().strip())
visited = {graph[s]: 0}

# Perform Prim's algorithm on graph
while len(visited) != n:
    lowestCost = (None, float('inf'))
    for node in visited:
        for nextNode,weight in node.connections.items():
            if nextNode not in visited and weight < lowestCost[1]:
                lowestCost = (nextNode, weight)
    
    node, weight = lowestCost
    visited[node] = weight
    
print(sum(visited.values()))