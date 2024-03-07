# https://school.programmers.co.kr/learn/courses/30/lessons/181188
# 이 문제 유형 생각 해봐야할 듯. 이런 유형을 지금 2개 째 못품...
# Greedy는 생각했었는데 Sweeping 알고리즘을 함께 사용.
# Start, End 이벤트마다 Greedy를 적용하면 되는 거였음.
from collections import defaultdict
import queue

def solution(targets):
    answer = 0
    misileEnd = queue.PriorityQueue()
    misiles = defaultdict(list)
    for target in targets:
        s, e = target
        misiles[s].append(e)

    misileStarts = sorted(misiles.keys())
    for start in misileStarts:
        if len(misileEnd.queue) > 0 and misileEnd.queue[0] <= start: 
            misileEnd.queue.clear()
            answer += 1
        for end in misiles[start]:
            misileEnd.put(end)

    print(answer)
    return answer + 1
    
targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
solution(targets)
