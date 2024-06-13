def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3, 4],
    4: []
}

start_node_0 = 0
reachable_from_0 = dfs(graph, start_node_0)
print(f"Les nœuds atteignables à partir de {start_node_0} sont : {reachable_from_0}")

start_node_3 = 3
reachable_from_3 = dfs(graph, start_node_3)
print(f"Les nœuds atteignables à partir de {start_node_3} sont : {reachable_from_3}")
