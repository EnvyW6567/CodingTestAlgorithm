import sys
import math

N = int(sys.stdin.readline())
count = 0
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if math.sqrt(i).is_integer():
        dp[i] = 1
    else:


print(count)


