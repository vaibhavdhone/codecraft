def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:

        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')
