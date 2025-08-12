import sys
import heapq
from collections import defaultdict

problemsHard = []
problemsEasy = []
solvedCount = 0
solvedProblems = defaultdict(int)


def recommend(x):
    if x == 1:
        hardL, hardP = problemsHard[0]
        if solvedProblems[hardP] == 1:
            problemsHard.pop(0)

            return recommend(x)
        print(hardP)

    if x == -1:
        easyL, easyP = problemsEasy[0]
        if solvedProblems[-easyP] == 1:
            problemsEasy.pop(0)

            return recommend(x)
        print(-easyP)


def add(P, L):
    heapq.heappush(problemsEasy, [int(L), int(P)])
    heapq.heappush(problemsHard, [-int(L), -int(P)])

    print(problemsHard)
    print(problemsEasy)


def solved(P):
    solvedProblems[P] = 1

    global solvedCount
    solvedCount += 1

    global problemsHard
    global problemsEasy
    if solvedCount == len(problemsHard):
        problemsHard = []
        problemsEasy = []


N = sys.stdin.readline()

for _ in range(int(N)):
    line = sys.stdin.readline()
    inputP, inputL = line.split(' ')
    add(int(inputP), int(inputL))

print(problemsHard)
print(problemsEasy)

M = sys.stdin.readline()

for _ in range(int(M)):
    line = sys.stdin.readline()
    command = line.split(' ')
    if command[0] == 'add':
        add(int(command[1]), int(command[2]))
    elif command[0] == 'solved':
        solved(int(command[1]))
    elif command[0] == 'recommend':
        recommend(int(command[1]))

