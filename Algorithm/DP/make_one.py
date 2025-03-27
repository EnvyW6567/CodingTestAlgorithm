import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque([N])
calculated = {N: 0}

while queue:
    num = queue.popleft()
    if num % 2 == 0 and num // 2 not in calculated:
        queue.append(num // 2)
        calculated[num // 2] = calculated[num] + 1
    if num % 3 == 0 and num // 3 not in calculated:
        queue.append(num // 3)
        calculated[num // 3] = calculated[num] + 1
    if num - 1 not in calculated:
        queue.append(num - 1)
        calculated[num - 1] = calculated[num] + 1
    if 1 in calculated:
        break

print(calculated[1])
