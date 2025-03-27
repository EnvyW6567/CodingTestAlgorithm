import sys
from collections import deque


def push_back(value):
    d.append(value)


def push_front(value):
    d.appendleft(value)


def pop_front():
    if empty() == 0:
        return d.popleft()
    return -1


def pop_back():
    if empty() == 0:
        return d.pop()
    return -1


def size():
    return len(d)


def front():
    if empty() == 0:
        return d[0]
    return -1


def back():
    if empty() == 0:
        return d[len(d) - 1]
    return -1


def empty():
    if len(d) == 0:
        return 1
    return 0


d = deque()
commands = {
    'push_back': push_back,
    'push_front': push_front,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'front': front,
    'back': back,
    'empty': empty
}

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        commands[command[0]](command[1])
    else:
        print(commands[command[0]]())
