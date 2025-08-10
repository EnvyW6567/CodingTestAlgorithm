import sys


def solution(tems, r):
    i, j, tem_sum = r - 1, -1, sum(tems[:r])
    answer = tem_sum

    while i < len(tems) - 1:
        i += 1
        j += 1

        tem_sum += tems[i]
        tem_sum -= tems[j]

        answer = max(tem_sum, answer)

    return answer


N, K = map(int, sys.stdin.readline().split())
tems = list(map(int, sys.stdin.readline().split()))

print(solution(tems, K))
