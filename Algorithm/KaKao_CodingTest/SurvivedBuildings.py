def isInside(cur, startEdge, endEdge, degree):
    if startEdge[0] <= cur[0] and cur[0] <= endEdge[0]:
        if startEdge[1] <= cur[1] and cur[1] <= endEdge[1]:
            return degree
    return 0


def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])

    for i in range(N):
        for j in range(M):
            sum = board[i][j]
            for s in skill:
                type = s[0]
                startEdge = [s[1], s[2]]
                endEdge = [s[3], s[4]]
                if type == 1:
                    degree = -1 * s[5]
                else:
                    degree = s[5]

                sum += isInside([i, j], startEdge, endEdge, degree)
            if sum > 0:
                answer += 1
    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2],
         [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))
