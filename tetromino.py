# https://www.acmicpc.net/problem/14500
import sys
from itertools import combinations


def find_next(r, c):
    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    nexts = []

    for mr, mc in move:
        if 0 <= r + mr < row and 0 <= c + mc < col:
            nexts.append((r + mr, c + mc))

    return nexts


def find(r, c):
    max_sum = 0
    visited = {}

    stack = [(r, c, 1, graph[r][c])]
    while stack:
        cur_r, cur_c, depth, s = stack.pop()
        visited[(cur_r, cur_c)] = True

        if depth == 4:
            max_sum = max(max_sum, s)
            continue

        nexts = find_next(cur_r, cur_c)

        for next_r, next_c in nexts:
            if (next_r, next_c) not in visited:
                stack.append((next_r, next_c, depth + 1, s + graph[next_r][next_c]))

    return max_sum


def find_fu(r, c):
    nexts = find_next(r, c)
    max_sum = 0

    if len(nexts) > 2:
        combs = combinations(nexts, 3)
        for comb in combs:
            s = graph[r][c]
            for cr, cc, in comb:
                s += graph[cr][cc]
            max_sum = max(max_sum, s)

    return max_sum


def solution(row, col):
    answer = 0
    for r in range(row):
        for c in range(col):
            answer = max(answer, find(r, c))
            answer = max(answer, find_fu(r, c))

    return answer


row, col = map(int, sys.stdin.readline().split())

graph = []

for _ in range(row):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(solution(row, col))
