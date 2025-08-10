import sys


def solution(m, foods):
    gaps, divisors = [], []

    for i in range(len(foods)):
        if i < len(foods) - 1:
            gaps.append(foods[i + 1] - foods[i])
        else:
            gaps.append(m - foods[i] + foods[0])

    for i in range(1, len(gaps)):
        if len(gaps) % i == 0:
            divisors.append(i)

    for divisor in divisors:
        flag = True
        rule = gaps[:divisor]
        for i in range(1, len(gaps) // divisor):
            if rule != gaps[i * divisor: (i + 1) * divisor]:
                flag = False
        if flag:
            return sum(rule)
    return sum(gaps)


T = int(sys.stdin.readline())

for _ in range(T):
    M, N = map(int, sys.stdin.readline().split())
    foods = []

    for _ in range(N):
        food = int(sys.stdin.readline())
        foods.append(food)

    print(solution(M, foods))
