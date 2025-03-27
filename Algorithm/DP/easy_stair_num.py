import sys

N = int(sys.stdin.readline())

fibo = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(N - 1):
    tmp = [0 for _ in range(10)]
    for j, f in enumerate(fibo[i]):
        if j == 0:
            tmp[j + 1] += fibo[i][j]
        elif j == 9:
            tmp[j - 1] += fibo[i][j]
        else:
            tmp[j + 1] += fibo[i][j]
            tmp[j - 1] += fibo[i][j]
    fibo.append(tmp)

print(sum(fibo[N - 1]) % 1000000000)
