from collections import defaultdict
import heapq

course = defaultdict(list)


def map_course(paths):
    for path in paths:
        i, j, w = path
        course[i].append([w, j])
        course[j].append([w, i])


def bfs(start, summits):
    heap = [[0, start]]
    visited = {start: 0}

    while heap:
        cur_intense, cur_loc = heapq.heappop(heap)
        if cur_loc in summits or (cur_loc in visited and cur_intense > visited[cur_loc]):
            continue

        for next_intense, next_loc in course[cur_loc]:
            intense = max(cur_intense, next_intense)
            if next_loc in visited:
                if intense < visited[next_loc]:
                    visited[next_loc] = intense
                    heapq.heappush(heap, [intense, next_loc])
            else:
                visited[next_loc] = intense
                heapq.heappush(heap, [intense, next_loc])

    return visited


def solution(n, paths, gates, summits):
    answer = [0, 10000001]
    map_course(paths)

    for gate in gates:
        visited = bfs(gate, summits)
        for summit in sorted(summits):
            _, intensity = answer
            if intensity > visited[summit]:
                answer = [summit, visited[summit]]

    return answer


print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
