import sys

N = int(sys.stdin.readline())
answer = [0, 1]

for i in range(N):
    answer.append(answer[i] + answer[i + 1])

print(answer[N + 1] % 10007)
