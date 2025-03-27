# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import defaultdict


def solution(n, wires):
    answer = n
    children = []
    for deleted_wire in wires:
        tree = defaultdict(list)
        for wire in wires:
            if wire != deleted_wire:
                tree[wire[0]].append(wire[1])
                tree[wire[1]].append(wire[0])
        num = dfs(1, tree)
        if answer > abs(n / 2 - num):
            answer = abs(n / 2 - num)

    return answer * 2


def dfs(start, tree):
    children_num = 0
    stack = [start]
    visited = {}
    while stack:
        cur_node = stack.pop()
        for node in tree[cur_node]:
            if node not in visited:
                stack.append(node)
                visited[node] = True
                children_num += 1
    return children_num


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
