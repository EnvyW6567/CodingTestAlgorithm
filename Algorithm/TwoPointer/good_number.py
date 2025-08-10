import sys
from collections import defaultdict


def solution(nums):
    s_dict = defaultdict(list)
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            s = nums[i] + nums[j]
            s_dict[s].append((i, j))

    for k, num in enumerate(nums):
        if num in s_dict:
            for i, j in s_dict[num]:
                if i != k and j != k:
                    answer += 1
    return answer


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print(solution(nums))
