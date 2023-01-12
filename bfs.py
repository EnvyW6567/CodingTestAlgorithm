from collections import deque


def bfs(graph, start):

    visited = []
    queue = deque([])
    queue.append(start)
    while queue:
        node = queue.popleft()
        visited.append(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    return visited


graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

start = 1

visited = bfs(graph, start)
print(visited)
