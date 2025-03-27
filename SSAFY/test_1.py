from collections import defaultdict


def solution(nums, k):
    nums = sorted(nums)
    num_count = defaultdict(int)
    answer = []

    for num in nums:
        num_count[num] += 1

    for first in num_count:
        print(first, num_count[first])
        for second in nums:
            for i in range(num_count[first]):
                answer.append(first + second)

    return answer[k - 1]

numbers = [3, 2, 3]
print(solution(numbers, 6))
