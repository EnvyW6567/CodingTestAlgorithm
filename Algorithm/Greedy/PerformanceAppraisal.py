# https://school.programmers.co.kr/learn/courses/30/lessons/152995
from collections import defaultdict

def solution(scores):
    answer = -1
    hash = defaultdict(list)
    
    # 점수 배열을 해쉬맵 형식으로 변환하여 진행
    s1 = []
    for s in scores:
        if not hash[s[0]]:
            s1.append(s[0])
        hash[s[0]].append(s[1])
    s1.sort(reverse=True)

    max = 0
    survive = defaultdict(list) # 상여금 수령 대상자
    for idx in s1:
        hash[idx].sort()
        for s in hash[idx]:
            if s >= max:
                max = s
                survive[idx].append(s)

    # 원호가 애초에 상여금 수령 대상자가 아닌 경우 검증
    if scores[0][1] not in survive[scores[0][0]]: 
        return -1
    
    rank = [] # 상여금 수령 대상자의 인사 고과 점수 순위
    for idx in survive:
        for s in survive[idx]:
            rank.append(idx + s)
    rank.sort(reverse=True) # 순위 정렬

    # 원호의 순위 도출
    wanho = scores[0][0] + scores[0][1]
    for rank, r in enumerate(rank):
        if wanho == r:
            answer = rank + 1
            break

    return answer

scores = [[0, 0],[0, 0]]
print(f'answer : {solution(scores)}')