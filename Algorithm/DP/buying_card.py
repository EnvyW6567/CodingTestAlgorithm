import sys

N = int(sys.stdin.readline())

p = map(int, sys.stdin.readline().split())
cards = {i + 1:  value for i, value in enumerate(p)}
money = [0]

for i in range(1, N + 1):
    tmp = []
    for j in range(i):
        tmp.append(cards[i - j] + money[j])
    money.append(min(tmp))
print(money[N])

