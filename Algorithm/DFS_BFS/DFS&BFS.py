# 백준 1260번

import sys

from collections import deque

node, edge, root = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(node+1)]
for i in range(edge):
    s, d = map(int, sys.stdin.readline().split())
    # 양방향 구현
    graph[s].append(d)
    graph[d].append(s)

# 작은 수를 먼저 탐색 구현
for i in range(node+1):
    graph[i].sort()


# DFS 스택 자료구조 구현
def dfs(vertex, graph, visited=[]):
    if vertex not in visited:
        visited.append(vertex)

        print(vertex,  end=' ')
        for i in graph[vertex]:
            dfs(i, graph, visited)


# BFS 큐 자료구조 구현
def bfs(start, graph, visited=[]):
    queue = deque([start])
    visited.append(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
                visited.append(i)


dfs(root, graph)
print()
bfs(root, graph)
