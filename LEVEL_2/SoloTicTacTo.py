#https://school.programmers.co.kr/learn/courses/30/lessons/160585
FIRST = "O"
LATER = "X"

def solution(board):
    firstCount = 0
    laterCount = 0
    
    # 선, 후공 갯수 확인
    for row in range(3):
        for column in range(3):
            element = board[row][column]
            if element == FIRST:
                firstCount += 1
            elif element == LATER:
                laterCount += 1
    # 후공 > 선공 일 경우 불가능
    if laterCount > firstCount or laterCount + 1 < firstCount:
        return 0
    
    #선공 완료했는데 갯수 같을때
    if isCompleted(FIRST, board) and firstCount == laterCount:
        print("this? 1")
        return 0

    if isCompleted(LATER, board) and firstCount > laterCount:
        print("this? 2")
        return 0
    
    return 1

def isCompleted(player, board):
    diagonalRightCount = 0
    diagonalLeftCount = 0
    for row in range(3):
        rowCount = 0
        columnCount = 0
        if board[row][row] == player:
            diagonalRightCount += 1
        if board[row][2-row] == player:
            diagonalLeftCount += 1
        for column in range(3):
            if board[row][column] == player:
                rowCount += 1
            if board[column][row] == player:
                columnCount += 1
        if rowCount == 3 or columnCount == 3 or diagonalRightCount == 3 or diagonalLeftCount == 3:
            print(rowCount, columnCount, diagonalLeftCount, diagonalRightCount)
            return True
    return False

board = ["O.X", ".O.", "..X"]
print(solution(board))