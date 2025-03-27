import sys

N = int(sys.stdin.readline())

fibo = [1, 1]

for i in range(N - 1):
    fibo.append(fibo[i] * 2 + fibo[i + 1])

print(fibo[N] % 10007)
