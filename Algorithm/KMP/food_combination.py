# https://www.acmicpc.net/problem/10977 - 백준 / 음식 조합 세기
import sys


def solution(m, foods):
    gaps = []

    for i in range(len(foods)):
        if i < len(foods) - 1:
            gaps.append(foods[i + 1] - foods[i])
        else:
            gaps.append(m - foods[i] + foods[0])

    # gap 수열에서 반복 구간 찾기
    rule, i, j = [gaps[0]], 0, 0

    while j < len(gaps) - 1:
        j += 1

        if gaps[j] == rule[i]:
            i += 1
            if i > len(rule) - 1:
                i = 0
        else:
            if len(rule) > len(foods) // 2:
                return sum(gaps)

            rule = gaps[:len(rule) + 1]
            i = 0
            j = len(rule) - 1

    return sum(rule)


C = int(sys.stdin.readline())

for _ in range(C):
    M, N = map(int, sys.stdin.readline().split())
    foods = []

    for _ in range(N):
        food = int(sys.stdin.readline())
        foods.append(food)

    print(solution(M, foods))
