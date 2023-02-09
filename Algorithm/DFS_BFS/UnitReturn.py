#https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import defaultdict, deque

def bfs(map, start, sList):

    queue = deque([])
    time = 1
    queue.append(start)
    
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for n in map[node]:
                if sList[n] == w-1:
                    queue.append(n)
                    sList[n] = time
        time += 1
                    
    return sList

def solution(n, roads, sources, destination):
    answer = []
    map = defaultdict(list)
    visited = [0 for _ in range(n+1)]
    for r in roads:
        map[r[0]].append(r[1]) # 양방향 그래프 이기 때문에
        map[r[1]].append(r[0]) # 역방향도 그래프에 추가

    sList = [-1 for _ in range(n+1)]
    sList[destination] = 0
    sList = bfs(map, destination, sList)
    for s in sources:
        answer.append(sList[s])
    return answer

n = 5
roads = [[1, 2], [2,3], [3,4], [4,5]]
sources = [1, 2, 3, 4, 5]
destination = 3
print(solution(n, roads, sources, destination))