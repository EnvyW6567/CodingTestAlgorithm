def dfs(graph, start):
    stack = []
    visited = []
    stack.append(start)
    while stack:
        node = stack.pop()
        visited.append(node)

        for n in graph[node]:
            if n not in visited:
                print(n)
                stack.append(n)
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

print(dfs(graph, start))
