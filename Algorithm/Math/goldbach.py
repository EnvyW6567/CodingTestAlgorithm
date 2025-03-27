import sys
import math

nums = []

while True:
    nums.append(int(sys.stdin.readline()))
    if nums[len(nums) - 1] == 0:
        break

max_num = max(nums)
arr = [0 for _ in range(max_num + 1)]
arr[0], arr[1] = 1, 1

primes = {}

for i in range(2, int(math.sqrt(max_num))):
    for j in range(i * 2, max_num + 1, i):
        arr[j] = 1

for idx, a in enumerate(arr):
    if a == 0:
        primes[idx] = True

for num in nums:
    for prime in primes:
        if num - prime in primes:
            print(f"{num} = {prime} + {num - prime}")
            break
