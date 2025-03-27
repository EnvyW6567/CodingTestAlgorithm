# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    total = 0
    start = 0
    for i in range(len(sequence)):
        if sequence[i] == k:
            return [i, i]
        total += sequence[i]
        if total == k:
            if answer[1] - answer[0] > i - start:
                answer = [start, i]

        while total >= k:
            total -= sequence[start]
            start += 1
            if total == k:
                if answer[1] - answer[0] > i - start:
                    answer = [start, i]

    return answer


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
