# https://www.acmicpc.net/problem/14501
# 퇴사
from collections import defaultdict

N = int(input())

schedule = []

for i in range(N):
    schedule.append(map(int, input().split()))

dp = [0 for _ in range(N + 1)]
max_p = 0
trigger = defaultdict(list)

for i, (t, p) in enumerate(schedule):
    # 트리거 등록
    trigger[t + i].append([i, p])
    dp[i + 1] = max_p
    if i + 1 not in trigger:
        continue

    ends = trigger[i + 1]
    for start_t, pe in ends:
        max_p = max(max_p, dp[start_t] + pe)
        dp[i + 1] = max_p

print(max_p)
