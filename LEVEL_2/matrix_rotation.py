# https://school.programmers.co.kr/learn/courses/30/lessons/77485
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            count += 1
            matrix[i][j] = count

    for query in queries:
        row_start, column_start, row_end, column_end = query
        range_num = []
        before = matrix[row_start][column_start]

        for column in range(column_start + 1, column_end + 1):
            matrix, before = change_matrix(matrix, row_start, column, before)
            range_num.append(before)
        for row in range(row_start + 1, row_end + 1):
            matrix, before = change_matrix(matrix, row, column_end, before)
            range_num.append(before)
        for column in range(column_end - 1, column_start - 1, -1):
            matrix, before = change_matrix(matrix, row_end, column, before)
            range_num.append(before)
        for row in range(row_end - 1, row_start - 1, -1):
            matrix, before = change_matrix(matrix, row, column_start, before)
            range_num.append(before)
        answer.append(min(range_num))

    return answer


def change_matrix(matrix, row, column, before):
    tmp = before
    before = matrix[row][column]
    matrix[row][column] = tmp
    return matrix, before


solution(100, 97, [[1, 1, 100, 97]])
