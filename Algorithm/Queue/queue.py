import sys
from collections import deque


def push(value):
    queue.append(value)


def pop():
    if empty() == 0:
        return queue.popleft()
    return -1


def size():
    return len(queue)


def empty():
    if len(queue) == 0:
        return 1
    return 0


def front():
    if empty() == 0:
        return queue[0]
    return -1


def back():
    if empty() == 0:
        return queue[len(queue) - 1]
    return -1


N = int(sys.stdin.readline())
queue = deque()

commands = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

for _ in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        commands[command[0]](command[1])
        continue
    print(commands[command[0]]())
