# https://www.acmicpc.net/problem/1062
# 가르침
from collections import defaultdict


def solution(n, k):
    answer = 0

    if k < 5:
        return 0

    dictionary = defaultdict(int)
    used_list = []

    for _ in range(n):
        word = input()
        used = {}
        if word == 'antatica':
            answer += 1
            continue

        for w in word:
            if w not in used and w not in 'antic':
                dictionary[w] += 1
                used[w] = True

        if len(used) == 0:
            answer += 1
        else:
            used_list.append(used)

    sorted_dict = sorted(dictionary.keys(), key=lambda x: dictionary[x], reverse=True)
    teached = sorted_dict[:k - 5]
    print(dictionary)
    print(teached)

    for used in used_list:
        flag = True
        for w in used:
            if w not in teached:
                flag = False
                break
        if flag:
            answer += 1
    return answer


N, K = map(int, input().split())

print(solution(N, K))
