from collections import defaultdict
from collections import deque


def bfs(start, graph, n):
    queue = deque([start])
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] += visited[vertex]+1
    return visited


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        # 양방향 구현
        graph[a].append(b)
        graph[b].append(a)
    maxedge = bfs(1, graph, n)
    m = max(maxedge)
    print(maxedge)
    answer = 0
    for i in maxedge:
        if i == m:
            answer += 1
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)
