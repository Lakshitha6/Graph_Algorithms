import random

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

result = []

def breadth_first_search(vertex):
    visited = [vertex]
    queue = [vertex]

    while queue:
        queue_out = queue.pop(0)
        result.append(queue_out)

        neighbors = graph[queue_out][:]  # Copy of adjacent vertices for a particular node
        random.shuffle(neighbors)      # shuffle for get different output at each run

        for adjacentVertex in neighbors:
            if adjacentVertex not in visited:
                queue.append(adjacentVertex)
                visited.append(adjacentVertex)


breadth_first_search('A')
print(result)