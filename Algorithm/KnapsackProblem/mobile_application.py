# https://www.acmicpc.net/problem/7579

"""
중요 포인트

    1. 어떤 값을 무게로두고 어떤 값을 가치로 둘 것인지 판단하기
    2. dp 배열에서 정답 탐색을 어떻게 할 것인지
"""

import sys


def solution(n, target_mem, mems, costs):
    total_cost = sum(costs)

    dp = [0 for _ in range(total_cost + 1)]

    for i in range(n):
        for cost in range(total_cost, costs[i] - 1, -1):
            dp[cost] = max(dp[cost], dp[cost - costs[i]] + mems[i])

    for i in range(total_cost + 1):
        if dp[i] >= target_mem:
            return i


n, target_mem = map(int, sys.stdin.readline().split())
mems = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

print(solution(n, target_mem, mems, costs))
