import sys

n, target_weight = map(int, sys.stdin.readline().split())

weights, values = [], []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weights.append(w)
    values.append(v)

dp = [0 for _ in range(target_weight + 1)]

for i in range(n):
    for w in range(target_weight, weights[i] - 1, -1):
        dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

print(dp[target_weight])
