import sys
import random

# 랜덤 Array 생성


def randomArray(input):
    rArray = []
    for i in range(input):
        rArray.append(i)
    for i in range(input):
        k = random.randint(0, input-1)
        tmp = rArray[i]
        rArray[i] = rArray[k]
        rArray[k] = tmp
    return rArray


def swap(a, b):
    return b, a


input = int(sys.stdin.readline())
ranArray = randomArray(input)
print(f'정렬 전 : {ranArray}')

# Bubble Sort
# for i in range(input):
#     for j in range(1, input-i):
#         if ranArray[j] < ranArray[j-1]:
#             ranArray[j], ranArray[j - 1] = swap(ranArray[j], ranArray[j-1])
# print(f'Bubble 정렬 후 : {ranArray}')

# Selection Sort
# for i in range(input):
#     min = ranArray[i]
#     minAddr = i
#     for j in range(i+1, input):
#         if min > ranArray[j]:
#             minAddr = j
#             min = ranArray[j]
#     ranArray[i], ranArray[minAddr] = swap(ranArray[i], ranArray[minAddr])
# print(f'Selection 정렬 후 : {ranArray}')

# Insertion Srot
for i in range(1, input):
    for j in range(i, 0, -1):
        if ranArray[j] < ranArray[j-1]:
            ranArray[j], ranArray[j-1] = swap(ranArray[j], ranArray[j-1])
        else:
            break
print(f'Insertion 정렬 후 : {ranArray}')
