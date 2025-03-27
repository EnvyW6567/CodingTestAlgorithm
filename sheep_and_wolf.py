# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict

SHEEP = 0
WOLF = 1


def solution(info, edges):
    answer = 0
    graph = defaultdict(list)
    for node in edges:
        graph[node[0]].append(node[1])

    sheep_num = dfs(0, info, graph)
    return sheep_num


# 양이 있는 노드까지 거쳐가는 늑대의 수 계산
def dfs(start, info, graph):
    wolves_num = 0
    sheep_num = 0
    later = defaultdict(list)
    stack = [start]
    while len(stack) > 0:
        cur_node = stack.pop()
        print(cur_node, graph[cur_node])
        if info[cur_node] == SHEEP:
            if later[sheep_num]:
                for node in later[sheep_num]:
                    stack.append(node)
            sheep_num += 1
        else:
            wolves_num += 1

        for node in graph[cur_node]:
            if info[node] == WOLF:
                if sheep_num <= wolves_num + 1:
                    later[wolves_num + 1].append(node)
                else:
                    stack.append(node)
            else:
                stack.append(node)

    return sheep_num


print("answer : ", solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                            [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
