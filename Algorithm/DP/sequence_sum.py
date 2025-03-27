import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
max_sum = 0
cur_sum = 0

for num in nums:
    if cur_sum + num < 0:
        cur_sum = 0
    else:
        cur_sum += num
        if cur_sum > max_sum:
            max_sum = cur_sum

print(max_sum)
