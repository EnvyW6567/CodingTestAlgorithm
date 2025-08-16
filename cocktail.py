# https://www.acmicpc.net/problem/1033
# 칵테일
from collections import defaultdict, deque

from math import gcd, lcm

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b, p, q = map(int, input().split())

    g = gcd(p, q)
    p //= g
    q //= g

    graph[a].append((b, p, q))
    graph[b].append((a, q, p))

queue = deque([0])
visited = {0: True}
cocktail = [0 for _ in range(N)]

while queue:
    cur = queue.popleft()

    next_arr = graph[cur]
    for n, p, q in next_arr:
        if n in visited:
            continue

        visited[n] = True
        queue.append(n)

        if cocktail[cur] == 0:
            cocktail[cur] = p
            cocktail[n] = q

        cur_p = cocktail[cur]
        lc = lcm(cocktail[cur], p)
        cocktail[n] = q * lc // p
        m = lc // cocktail[cur]
        for idx, c in enumerate(cocktail):
            if idx == n:
                continue
            cocktail[idx] = c * m

print(" ".join(str(item) for item in cocktail))
