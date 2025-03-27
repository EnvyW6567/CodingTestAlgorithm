# https://school.programmers.co.kr/learn/courses/30/lessons/169198

# Algorithm: Greedy

"""
문제 포인트:
    5 보다 큰 자릿수 -> 10 - 자릿수 -> 다음 자릿수 + 1
    5 보다 작거나 같은 자릿수
      - 만약 다음 자릿수가 5보다 클 경우 -> 10 - 자릿수 -> 다음 자릿수 + 1
      - else -> 자릿수

"""


def solution(storey):
    answer = 0

    s_list = []  # 자릿수 리스트

    while storey > 0:
        s_list.append(storey % 10)
        storey //= 10

    s_list.append(0)
    for i, s in enumerate(s_list):
        if s == 10:
            s_list[i + 1] += 1
            continue

        if s > 5 or (s == 5 and s_list[i + 1] >= 5):
            answer += 10 - s
            if i < len(s_list) - 1:
                s_list[i + 1] += 1
        else:
            answer += s

    return answer
