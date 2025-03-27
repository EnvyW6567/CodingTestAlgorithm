# https://school.programmers.co.kr/learn/courses/30/lessons/12899
import math


def solution(n):
    rule = {0: 1, 1: 1, 2: 2, 3: 4}
    n -= 1
    num = []
    while n > 0:
        print(n, n % 4)
        num.append(rule[n % 4])
        n = n // 3
    print(num)


solution(14)
