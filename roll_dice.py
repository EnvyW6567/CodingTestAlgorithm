# https://www.acmicpc.net/problem/14499
# 주사위 굴리기
from collections import deque

world = []
mr, mc, r, c, k = map(int, input().split())

for i in range(mr):
    world.append(list(map(int, input().split())))

orders = list(map(int, input().split()))

dice = [deque([0, 0, 0, 0]), deque([0, 0, 0, 0])]
direction = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
cur_loc = [r, c]

for order in orders:
    new_loc = [x + y for x, y in zip(cur_loc, direction[order])]

    if mr <= new_loc[0] or new_loc[0] < 0 or mc <= new_loc[1] or new_loc[1] < 0:
        continue

    cur_loc = new_loc

    ii, mm = dice
    if order == 1:
        mm.appendleft(mm.pop())
        ii[1] = mm[1]
        ii[3] = mm[3]

    elif order == 2:
        mm.append(mm.popleft())
        ii[1] = mm[1]
        ii[3] = mm[3]

    elif order == 3:
        ii.append(ii.popleft())
        mm[1] = ii[1]
        mm[3] = ii[3]

    elif order == 4:
        ii.appendleft(ii.pop())
        mm[1] = ii[1]
        mm[3] = ii[3]

    floor = mm[3]
    if world[cur_loc[0]][cur_loc[1]] == 0:
        world[cur_loc[0]][cur_loc[1]] = floor
    else:
        floor = world[cur_loc[0]][cur_loc[1]]
        mm[3] = floor
        ii[3] = floor
        floor = 0
        world[cur_loc[0]][cur_loc[1]] = 0

    print(mm[1])
