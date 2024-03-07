from collections import deque


def solution(board, moves):
    crane = deque(deque() for _ in range(len(board)))
    before = 0
    answer = 0
    bucket = []
    for i in board:
        for idx, j in enumerate(i):
            if j > 0:
                crane[idx].append(j)
    print(crane)
    for m in moves:
        i = m-1
        if len(crane[i]) != 0:
            cur = crane[i].popleft()
            if cur != before:
                bucket.append(cur)
                before = cur
            else:
                bucket.pop
                answer += 2
                if len(bucket) == 0:
                    before = 0
                else:
                    before = bucket[len(bucket)-1]
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
