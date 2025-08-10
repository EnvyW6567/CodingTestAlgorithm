# https://www.acmicpc.net/problem/9084

import sys


def solution(n, coins, cost):
    dp = [0 for _ in range(cost + 1)]

    for coin in coins:
        if coin > cost:
            break
        dp[coin] += 1
        for c in range(coin, cost + 1):
            dp[c] += dp[c - coin]

    return dp[cost]


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    cost = int(sys.stdin.readline())
    print(solution(n, coins, cost))
