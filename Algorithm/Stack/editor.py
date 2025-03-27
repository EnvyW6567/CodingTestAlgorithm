import sys


def left():
    if len(editor) > 0:
        remains.append(editor.pop())


def right():
    if len(remains) > 0:
        editor.append(remains.pop())


def backspace():
    if len(editor) > 0:
        editor.pop()


def put(word):
    editor.append(word)


beginning = list(sys.stdin.readline().strip())
remains = []
editor = []

for b in beginning:
    editor.append(b)

N = int(sys.stdin.readline())

commands = {
    'L': left,
    'D': right,
    'B': backspace,
    'P': put
}

for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        commands[command[0]](command[1])
        continue
    commands[command[0]]()

for e in editor:
    print(e, end='')
while len(remains) > 0:
    print(remains.pop(), end='')
