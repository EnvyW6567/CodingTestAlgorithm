# https://school.programmers.co.kr/learn/courses/30/lessons/12936
import math


def solution(n, k):
    answer = []
    line = [i + 1 for i in range(n)]
    while n > 1:
        line_idx = math.ceil(k / math.factorial(n - 1)) - 1
        answer.append(line[line_idx])
        del line[line_idx]
        k = k % math.factorial(n - 1)
        n = n - 1
    answer.append(line[0])

    print(answer)
    return answer


solution(3, 5)
