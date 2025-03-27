# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from collections import defaultdict
from itertools import combinations


def solution(orders, courses):
    answer = []
    for course in courses:
        menu = defaultdict(int)
        max = 2
        for order in orders:
            order = sorted(list(order))
            comb = combinations(order, course)
            for c in comb:
                menu[c] += 1
        for m in menu:
            if menu[m] >= max:
                max = menu[m]
        for m in menu:
            if menu[m] == max:
                answer.append(''.join(m))

    return sorted(answer)


solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
