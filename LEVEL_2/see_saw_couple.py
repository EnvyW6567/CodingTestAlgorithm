# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import defaultdict


def solution(weights):
    # 4배, 2배, 1배, 3/2배, 4/3배
    answer = 0
    possible_mag = [2, 3 / 2, 4 / 3]
    w_map = defaultdict(int)
    for weight in weights:
        w_map[weight] += 1

    weights = list(w_map.keys())
    for weight in weights:
        if w_map[weight] > 1:
            answer += int(w_map[weight] * (w_map[weight] - 1) / 2)
        for p in possible_mag:
            couple_weight = weight * p
            if couple_weight in w_map:
                answer += w_map[couple_weight] * w_map[weight]
    return answer


solution([100, 180, 360, 100, 270])
