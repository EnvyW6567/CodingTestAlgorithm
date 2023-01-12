# 백준 1700번

import sys

m, n = map(int, sys.stdin.readline().split())
schedule = list(map(int, sys.stdin.readline().split()))

count = 0
using = []

for i in range(n):
    if schedule[i] in using:
        continue

    if len(using) != m:
        using.append(schedule[i])
        continue

    far = 0
    tmp = 0

    for plug in using:
        if plug not in schedule[i:]:
            tmp = plug
            break
        elif schedule[i:].index(plug) > far:
            far = schedule[i:].index(plug)
            tmp = plug
    using[using.index(tmp)] = schedule[i]
    count += 1
print(count)
