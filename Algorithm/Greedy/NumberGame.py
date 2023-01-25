from collections import deque


def solution(A, B):

    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    size = len(A)

    for _ in range(size):

        if(A[len(A)-1] < B[len(B)-1]):
            A.pop()
            B.pop()
            answer += 1
        else:
            A.pop()
            B.popleft()

    return answer


A = [5, 7, 6, 5, 4, 2, 3]
B = [8, 6, 5, 2, 3, 5, 4]
solution(A, B)
