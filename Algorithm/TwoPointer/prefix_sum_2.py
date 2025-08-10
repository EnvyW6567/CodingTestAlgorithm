import sys


def solution(nums, target):
    answer, cur_sum, j = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == target:
            answer += 1
            j = i
            continue

        elif nums[i] > target:
            j = i
            continue

        cur_sum += nums[i]
        if cur_sum == target:
            answer += 1
            continue

        elif cur_sum > target:
            while i > j and cur_sum > target:
                cur_sum -= nums[j]
                j += 1
                if cur_sum == target:
                    answer += 1

    return answer


_, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

print(solution(nums, M))
