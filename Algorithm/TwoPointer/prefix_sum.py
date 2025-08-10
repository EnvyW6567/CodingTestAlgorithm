# https://www.acmicpc.net/problem/1806

import sys


def solution(nums, min_sum):
    answer, cur_sum, j = 0, nums[0], 0

    if cur_sum >= min_sum:
        return 1

    for i in range(1, len(nums)):
        if nums[i] >= min_sum:
            return 1

        cur_sum += nums[i]
        gap = i - j + 1

        if cur_sum >= min_sum:
            while i > j:
                cur_sum -= nums[j]
                j += 1
                if cur_sum >= min_sum:
                    gap -= 1
                else:
                    break

            if answer == 0:
                answer = gap
            else:
                answer = min(answer, gap)
    return answer


N, S = map(int, sys.stdin.readline().split(' '))
nums = list(map(int, sys.stdin.readline().split()))

print(solution(nums, S))
