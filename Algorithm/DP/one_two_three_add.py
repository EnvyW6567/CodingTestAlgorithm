import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    fibo = [0, 0, 1]
    for i in range(num):
        fibo.append(fibo[i] + fibo[i + 1] + fibo[i + 2])
    print(fibo[len(fibo) - 1])

