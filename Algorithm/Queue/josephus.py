import sys

N, K = map(int, sys.stdin.readline().split())

tmp = []
answer = []
queue = [i + 1 for i in range(N)]
count = 1
iterator = 0

while queue:
    if count == K:
        answer.append(queue[iterator])
        count = 1
    else:
        tmp.append(queue[iterator])
        count += 1

    if iterator == len(queue) - 1:
        queue = tmp
        tmp = []
        iterator = 0
    else:
        iterator += 1

print(f"<{", ".join(map(str, answer))}>")
