# https://www.acmicpc.net/problem/1034
# 램프
from collections import defaultdict

N, M = map(int, input().split())
lamps = []

for _ in range(N):
    lamps.append(input())

k = int(input())
lamp_status = defaultdict(int)

for row in lamps:
    need_click = []
    for i, lamp in enumerate(row):
        if lamp == '0':
            need_click.append(i)

    lamp_status[tuple(need_click)] += 1

answer = 0

for colums in lamp_status:
    if len(colums) <= k:
        if len(colums) % 2 == k % 2:
            answer = max(lamp_status[colums], answer)

print(answer)
