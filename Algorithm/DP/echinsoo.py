import sys

N = int(sys.stdin.readline())

fibo = [[0, 0], [0, 1], [1, 0]]

for i in range(2, N):
    fibo.append([fibo[i][0] + fibo[i][1], fibo[i][0]])

print(sum(fibo[N]))
