#https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict

def dfs(map, start, summitsCost, n, noEntry):
    visited = defaultdict(int)
    cost = [0 for _ in range(n+1)]
    stack = []
    stack.append(start)
    # print(summitsCost)
    while stack:
        curNode = stack.pop()
        for nextNode in map[curNode]: # nextNode[0] << 노드 번호 // nextNode[1] << 노드 비용
            # print(cost)
            if visited[nextNode[0]] == 0 and noEntry[nextNode[0]] == 0:

                if cost[curNode] < nextNode[1]:
                    cost[nextNode[0]] = nextNode[1] # 현재 노드 값과 다음 노드 비용 중 큰 값 선택
                else:
                    cost[nextNode[0]] = cost[curNode]

                if summitsCost[nextNode[0]] == 0:
                    stack.append(nextNode[0])
                    visited[nextNode[0]] = 1
                else:
                    if summitsCost[nextNode[0]] == 1:
                        summitsCost[nextNode[0]] = cost[nextNode[0]]
                    elif summitsCost[nextNode[0]] > cost[nextNode[0]]:
                        summitsCost[nextNode[0]] = cost[nextNode[0]]
    return summitsCost

def solution(n, paths, gates, summits):
    map = defaultdict(list)
    noEntry = defaultdict(int)
    summitsCost = defaultdict(int)
    
    for p in paths:
        map[p[0]].append([p[1], p[2]])# 양방향
        map[p[1]].append([p[0], p[2]])# 그래프

    for g in gates: # 출입구 방문 예외 처리
        noEntry[g] = 1
        
    for s in summits:
        summitsCost[s] = 1

    for g in gates:
        summitsCost = dfs(map, g, summitsCost, n, noEntry)
        # print(summitsCost)

    min = 10000000
    minSummit = 0
    for sc in summitsCost:
        if min > summitsCost[sc] and summitsCost[sc] != 0:
            minSummit = sc
            min = summitsCost[sc]
    answer = [minSummit, min]
    return answer

n = 6
paths =  [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
print(solution(n, paths, gates, summits))