from collections import deque


def compare(word, target, dic):
    count = 0
    for i in range(len(word)):
        if word[i] == target[i]:
            count += 1

    if count == len(word)-1:
        dic[word].append(target)

    return dic


def solution(begin, target, words):
    if target not in words:
        return 0

    words.append(begin)
    dic = {}
    for word in words:
        dic[word] = []

    for word in words:
        for targ in words:
            if word == targ:
                continue
            dic = compare(word, targ, dic)

    print(dic)
    answer = bfs(begin, dic, target, words)
    return answer


def bfs(start, graph, target, words, visited=[]):
    distance = {}
    for word in words:
        distance[word] = 0
        
    queue = deque([start])
    visited.append(start)
    count = 0
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if target in graph[vertex]:
                i = target
            if i not in visited:
                queue.append(i)
                visited.append(i)
                distance[i] = distance[vertex] + 1
                if i == target:
                    queue.clear()
                    return distance[i]
    return 0


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
