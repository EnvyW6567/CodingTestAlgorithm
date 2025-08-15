# https://www.acmicpc.net/problem/26500
# Absolutely
T = int(input())

for _ in range(T):
    a, b = map(float, input().split())

    print(round(abs(a - b), 1))
