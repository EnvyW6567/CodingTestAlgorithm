# https://www.acmicpc.net/problem/15591
import sys
from collections import defaultdict, deque

mootube = defaultdict(list)


def solution(K, start_node):
    answer = 0
    visited = {start_node: True}
    queue = deque(mootube[start_node])

    while queue:
        next_node, next_usado = queue.popleft()

        if next_node not in visited and K <= next_usado:
            answer += 1
            for n in mootube[next_node]:
                queue.append(n)
        visited[next_node] = True

    return answer


N, Q = map(int, sys.stdin.readline().split())
questions = []

for _ in range(N - 1):
    p, q, usado = map(int, sys.stdin.readline().split())  # p, q 동영상 사이의 거리(USADO) r
    mootube[p].append([q, usado])
    mootube[q].append([p, usado])

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(solution(k, v))
