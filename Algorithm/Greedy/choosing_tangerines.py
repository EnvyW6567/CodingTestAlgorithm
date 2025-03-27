# https://school.programmers.co.kr/learn/courses/30/lessons/138476

"""
문제 포인트
    dictionary 활용
"""
from collections import defaultdict
import heapq


def solution(k, tangerine):
    answer = 0
    tangerine_dict = defaultdict(int)
    tangerine_heap = []
    tangerine_count = 0

    for t in tangerine:
        tangerine_dict[t] += 1

    for _, v in tangerine_dict.items():
        heapq.heappush(tangerine_heap, -v)

    while tangerine_count < k:
        tangerine_count -= heapq.heappop(tangerine_heap)
        answer += 1

    return answer
