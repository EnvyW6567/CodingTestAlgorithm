# https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 에라이 씹빨 모르겠다 진짜
# 분명 노가다 하면 가능한데 이게 의도일 리가 없다.
from collections import defaultdict, deque

START = 'R'
WALL = 'D'
queue = deque()
visited = {}

def solution(board):
    answer = 0
    start = foundStart(board)
    
def foundStart(board):
    for row in board:
        for column in row:
            if board[row][column] == START:
                start = [row, column]
                return start

def up(node, board):
    nextNode = node
    while(not isWall(nextNode)):
        row, colum = nextNode

    
def isWall(node):
    row, column = node
    if board[row][column] == WALL or row < 0 or row > len(board) or column < 0 or column > len(board[0]):
        return True
    return False

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	
solution(board)