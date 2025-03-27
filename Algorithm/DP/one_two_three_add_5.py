import sys

N = int(sys.stdin.readline())
fibo = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(fibo) < num:
        for i in range(len(fibo), num):
            fibo.append([
                (fibo[i - 1][1] + fibo[i - 1][2]) % 1000000009,
                (fibo[i - 2][0] + fibo[i - 2][2]) % 1000000009,
                (fibo[i - 3][0] + fibo[i - 3][1]) % 1000000009,
            ])
    print(sum(fibo[num - 1]) % 1000000009)
