# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from collections import defaultdict


def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for r in road:
        town_a, town_b, distance = r
        graph[town_a].append([town_b, distance])
        graph[town_b].append([town_a, distance])

    return dfs(graph, 1, K)


def dfs(graph, start_node, K):
    stack = [start_node]
    visited = {1: 0}
    while len(stack) > 0:
        node = stack.pop()
        distance = visited[node]
        for next_node, next_distance in graph[node]:
            if next_node not in visited and distance + next_distance <= K:
                visited[next_node] = distance + next_distance
                stack.append(next_node)
            elif next_node in visited:
                if visited[next_node] > distance + next_distance:
                    visited[next_node] = distance + next_distance
                    stack.append(next_node)

    return len(visited)


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
