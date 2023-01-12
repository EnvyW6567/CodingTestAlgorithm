from collections import deque


def swap(a, b):
    return b, a


def Lchild(idx):
    return idx * 2 + 1


def Rchild(idx):
    return idx * 2 + 2


def parent(idx):
    return int((idx-1)/2)


# Heap 삽입 과정
'''
1) 마지막 노드에 삽입
2) 부모노드와 비교
3) 작을 경우 부모노드와 해당 노드 swap
4) 아닐 경우 return
'''


def insert(heap, idx):

    while(idx != 0):  # root노드 이전 까지 진행
        if heap[idx] < heap[parent(idx)]:
            heap[idx], heap[parent(idx)] = swap(heap[idx], heap[parent(idx)])
            idx = parent(idx)

        else:
            break

    return heap


'''
root 노드에 값을 삽입
최소힙 조건을 만족하도록 heapify진행
자식노드가 없을 때 까지 진행.
'''


def heapify(heap):

    idx = 0
    last_idx = len(heap) - 1
    while(Lchild(idx) < last_idx):  # 자식노드가 없을 경우 -> 왼쪽 자식노드가 heap의 길이보다 클경우.
        if heap[Lchild(idx)] < heap[Rchild(idx)]:
            if heap[idx] > heap[Lchild(idx)]:
                heap[idx], heap[Lchild(idx)] = swap(
                    heap[idx], heap[Lchild(idx)])
                idx = Lchild(idx)
            else:
                break
        else:
            if heap[idx] > heap[Rchild(idx)]:
                heap[idx], heap[Rchild(idx)] = swap(
                    heap[idx], heap[Rchild(idx)])
                idx = Rchild(idx)
            else:
                break

    return heap


'''
최솟값 삭제
root node를 pop해주고
root node에 마지막 노드 값을 삽입 후
heapify 진행
'''


def minDelete(heap):

    if len(heap) > 1:  # 노드가 2개 이상일 때
        heap[0] = heap.pop()
        heap = heapify(heap)
        return heap

    # 노드가 1개 일 때
    heap.pop()
    return heap


'''
자식 노드가 없는 노드에서 최댓값 비교
삭제 후 마지막 노드를 삽입
삽입 과정과 실행
'''


def maxDelete(heap):
    max = heap[len(heap)-1]  # 맨 마지막 노드부터 순차 탐색
    last_idx = len(heap) - 1  # 맨 마지막 노드
    idx = last_idx
    max_idx = last_idx
    # 자식노드가 없는 경우
    while(Lchild(idx) > last_idx):

        if max < heap[idx]:
            max = heap[idx]
            max_idx = idx

        idx -= 1

    if max_idx == len(heap) - 1:  # 맨 마지막 노드가 max 일 경우
        heap.pop()
        return heap

    heap[max_idx] = heap.pop()
    heap = insert(heap, max_idx)
    return heap


# def getMax(heap):
#     idx = len(heap)-1
#     max = heap[len(heap)-1]  # 맨 마지막 노드부터 순차 탐색
#     # 자식노드가 없는 경우
#     while(Lchild(idx) > len(heap)-1 and Rchild(idx) > len(heap)-1):

#         if idx == 0:
#             break

#         if max < heap[idx]:
#             max = heap[idx]

#         idx -= 1
#     return max


def solution(operations):

    heap = deque([])
    for op in operations:
        action, num = op.split(" ")

        if action == "I":
            heap.append(int(num))
            insert(heap, len(heap)-1)

        else:
            if(len(heap) != 0):
                if(num == "-1"):
                    minDelete(heap)
                else:
                    maxDelete(heap)
        print(f'{op:10} : {heap}')

    answer = []
    if len(heap) == 0:
        answer = [0, 0]
        return answer

    answer.append(max(heap))
    answer.append(heap[0])
    return answer


operations = ["I 1", "I 10", "I 3", "I 11",
              "I 13", "I 5", "I 6", "I 12", "I 12", "I 14", "I 15", "D -1"]
print(solution(operations))
