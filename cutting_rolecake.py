# https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""
문제 포인트
    토핑별 갯수 저장 -> dictionary 활용
    원 포인터로 갯수 확인 (좌측 -> 우측)
"""
from collections import defaultdict


def solution(topping):
    answer = 0
    topping_dict = defaultdict(int)
    left_cake, left_toppings, right_toppings = {}, 0, 0

    for t in topping:
        topping_dict[t] += 1

    right_toppings = len(topping_dict)

    for i in range(len(topping)):
        t = topping[i]
        if t not in left_cake:
            left_toppings += 1
            left_cake[t] = True

        topping_dict[t] -= 1

        if topping_dict[t] == 0:
            right_toppings -= 1

        if left_toppings == right_toppings:
            answer += 1

    return answer
