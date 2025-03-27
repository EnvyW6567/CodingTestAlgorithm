import sys

N = int(sys.stdin.readline())

stack = []


def push(value):
    stack.append(value)


def pop():
    return stack.pop() if len(stack) > 0 else -1


def top():
    return stack[len(stack) - 1] if len(stack) > 0 else -1


def size():
    return len(stack)


def empty():
    return 1 if len(stack) == 0 else 0


commands = {
    'push': push,
    'pop': pop,
    'top': top,
    'size': size,
    'empty': empty
}


for _ in range(N):
    line = sys.stdin.readline().split()
    command = line[0]
    if len(line) > 1:
        value = int(line[1])
        commands[command](value)

    else:
        print(commands[command]())


