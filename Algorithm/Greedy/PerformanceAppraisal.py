# https://school.programmers.co.kr/learn/courses/30/lessons/152995
from collections import defaultdict

def solution(scores):
    answer = -1
    hash = defaultdict(list)
    s1 = []
    for s in scores:
        if not hash[s[0]]:
            s1.append(s[0])
        hash[s[0]].append(s[1])
    s1.sort(reverse=True)
    max = 0
    survive = defaultdict(list)
    for idx in s1:
        hash[idx].sort()
        for s in hash[idx]:
            if s >= max:
                max = s
                survive[idx].append(s)

    if scores[0][1] not in survive[scores[0][0]]:
        return -1
    
    rank = []
    for idx in survive:
        for s in survive[idx]:
            rank.append(idx + s)
    rank.sort(reverse=True)
    wanho = scores[0][0] + scores[0][1]
    for rank, r in enumerate(rank):
        if wanho == r:
            answer = rank + 1
            break

    return answer

scores = [[0, 0],[0, 0]]
print(f'answer : {solution(scores)}')