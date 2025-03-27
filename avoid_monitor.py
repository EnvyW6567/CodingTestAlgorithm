import sys


# def solution():
#

# def monitor():
#     for row, col in teachers:



N = int(sys.stdin.readline())

passage = [[0 for _ in range(N)] for _ in range(N)]
students = {}
teachers = {}

for row in range(N):
    elements = sys.stdin.readline().split()
    for col, element in enumerate(elements):
        if element == 'T':
            teachers[(row, col)] = True
            passage[row][col] = -1

    passage.append(elements)

# solution()

# print("students")
# for s in students:
#     print(s)
# print("teachers")
# for t in teachers:
#     print(t)
print("passage")
for p in passage:
    print(p)
