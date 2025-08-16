# https://www.acmicpc.net/problem/1074
# Z
N, r, c = map(int, input().split())
answer = 0

for n in range(N - 1, -1, -1):
    seq = 0

    if r >= pow(2, n):
        seq += 2
        r -= pow(2, n)

    if c >= pow(2, n):
        seq += 1
        c -= pow(2, n)

    answer += seq * pow(2, n * 2)

print(answer)
