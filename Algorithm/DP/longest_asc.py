import sys
from collections import defaultdict

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
seq = [1 for _ in range(N)]
seqq = defaultdict(list)
for i, num in enumerate(nums):
    seqq[i] = [num]

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] < nums[j] and seq[i] <= seq[j]:
            seq[i] = seq[j] + 1
            seqq[i] = [nums[i]] + seqq[j]

print(max(seq))
for i in seqq[seq.index(max(seq))]:
    print(i, end=" ")
