import random

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

result = []

def depth_first_search(vertex):
    visited = [vertex]
    stack = [vertex]

    while stack:

        stack_out = stack.pop()
        result.append(stack_out)

        neighbors = graph[stack_out][:]  # Copy of adjacent vertices for a particular node
        random.shuffle(neighbors)  # shuffle for get different output at each run

        for adjacentVertex in neighbors:
            if adjacentVertex not in visited:
                stack.append(adjacentVertex)
                visited.append(adjacentVertex)


depth_first_search('A')
print(result)